# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['KeyArgs', 'Key']

@pulumi.input_type
class KeyArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 bits: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Key resource.
        :param pulumi.Input[str] type: Type of the key to generate one of RSA, ED25519, SECP256K1, ECDSA
        :param pulumi.Input[int] bits: Siye of the key (Only for RSA key)
        """
        pulumi.set(__self__, "type", type)
        if bits is not None:
            pulumi.set(__self__, "bits", bits)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type of the key to generate one of RSA, ED25519, SECP256K1, ECDSA
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def bits(self) -> Optional[pulumi.Input[int]]:
        """
        Siye of the key (Only for RSA key)
        """
        return pulumi.get(self, "bits")

    @bits.setter
    def bits(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bits", value)


class Key(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bits: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Key resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] bits: Siye of the key (Only for RSA key)
        :param pulumi.Input[str] type: Type of the key to generate one of RSA, ED25519, SECP256K1, ECDSA
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Key resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param KeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bits: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KeyArgs.__new__(KeyArgs)

            __props__.__dict__["bits"] = bits
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["peer_id"] = None
            __props__.__dict__["private"] = None
            __props__.__dict__["public"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["private"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Key, __self__).__init__(
            'libp2p:index:Key',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="peerId")
    def peer_id(self) -> pulumi.Output[str]:
        """
        Peer ID
        """
        return pulumi.get(self, "peer_id")

    @property
    @pulumi.getter
    def private(self) -> pulumi.Output[str]:
        """
        Marshalled private key
        """
        return pulumi.get(self, "private")

    @property
    @pulumi.getter
    def public(self) -> pulumi.Output[str]:
        """
        Marshalled public key
        """
        return pulumi.get(self, "public")

