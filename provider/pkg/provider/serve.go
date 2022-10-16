package provider

import (
	"github.com/pulumi/pulumi/pkg/v3/resource/provider"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/cmdutil"
)

func Serve(providerName, version string, schema []byte) {
	if err := provider.ComponentMain(providerName, version, schema, construct); err != nil {
		cmdutil.ExitError(err.Error())
	}
}
