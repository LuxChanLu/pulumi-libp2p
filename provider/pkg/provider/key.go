package provider

import (
	"github.com/libp2p/go-libp2p/core/crypto"
	"github.com/libp2p/go-libp2p/core/peer"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type KeyType pulumi.String

const (
	KeyTypeRSA       = KeyType("RSA")
	KeyTypeED25519   = KeyType("ED25519")
	KeyTypeSECP256K1 = KeyType("SECP256K1")
	KeyTypeECDSA     = KeyType("ECDSA")
)

var keyTypeMapping = map[KeyType]int{
	KeyTypeRSA:       crypto.RSA,
	KeyTypeED25519:   crypto.Ed25519,
	KeyTypeSECP256K1: crypto.Secp256k1,
	KeyTypeECDSA:     crypto.ECDSA,
}

type KeyArgs struct {
	Type pulumi.StringInput `pulumi:"type"`
	Bits pulumi.IntInput    `pulumi:"bits"`
}

type Key struct {
	pulumi.ResourceState

	PeerId  pulumi.StringOutput `pulumi:"peerId"`
	Private pulumi.StringOutput `pulumi:"private"`
	Public  pulumi.StringOutput `pulumi:"public"`
}

func NewKey(ctx *pulumi.Context,
	name string, args *KeyArgs, opts ...pulumi.ResourceOption) (*Key, error) {
	if args == nil {
		args = &KeyArgs{}
	}

	component := &Key{}
	err := ctx.RegisterComponentResource("libp2p:index:Key", name, component, opts...)
	if err != nil {
		return nil, err
	}

	if args.Bits == nil {
		args.Bits = pulumi.Int(0)
	}

	generated := pulumi.All(args.Type, args.Bits).ApplyT(func(args []interface{}) ([]string, error) {
		priv, pub, err := crypto.GenerateKeyPair(keyTypeMapping[KeyType(args[0].(string))], args[1].(int))
		if err != nil {
			return nil, err
		}
		peerId, err := peer.IDFromPublicKey(pub)
		if err != nil {
			return nil, err
		}
		privMarshal, err := crypto.MarshalPrivateKey(priv)
		if err != nil {
			return nil, err
		}
		pubMarshal, err := crypto.MarshalPublicKey(pub)
		if err != nil {
			return nil, err
		}
		return []string{peer.ToCid(peerId).String(), crypto.ConfigEncodeKey(privMarshal), crypto.ConfigEncodeKey(pubMarshal)}, nil
	}).(pulumi.StringArrayOutput)

	component.PeerId = generated.Index(pulumi.Int(0))
	component.Private = generated.Index(pulumi.Int(1))
	component.Public = generated.Index(pulumi.Int(2))

	if err := ctx.RegisterResourceOutputs(component, pulumi.Map{
		"peerId":  component.PeerId,
		"private": component.Private,
		"public":  component.Public,
	}); err != nil {
		return nil, err
	}

	return component, nil
}
