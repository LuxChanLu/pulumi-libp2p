package provider

import (
	"github.com/pkg/errors"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/provider"
)

func construct(ctx *pulumi.Context, typ, name string, inputs provider.ConstructInputs, options pulumi.ResourceOption) (*provider.ConstructResult, error) {
	switch typ {
	case "libp2p:index:Key":
		return constructKey(ctx, name, inputs, options)
	default:
		return nil, errors.Errorf("unknown resource type %s", typ)
	}
}

func constructKey(ctx *pulumi.Context, name string, inputs provider.ConstructInputs, options pulumi.ResourceOption) (*provider.ConstructResult, error) {
	args := &KeyArgs{}
	if err := inputs.CopyTo(args); err != nil {
		return nil, errors.Wrap(err, "setting args")
	}

	key, err := NewKey(ctx, name, args, options)
	if err != nil {
		return nil, errors.Wrap(err, "creating component")
	}

	return provider.NewConstructResult(key)
}
