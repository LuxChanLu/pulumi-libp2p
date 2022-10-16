//go:generate go run ./generate.go

package main

import (
	"github.com/pulumi/pulumi-libp2p/pkg/provider"
	"github.com/pulumi/pulumi-libp2p/pkg/version"
)

var providerName = "libp2p"

func main() {
	provider.Serve(providerName, version.Version, pulumiSchema)
}
