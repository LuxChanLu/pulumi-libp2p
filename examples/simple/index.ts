import * as libp2p from "@pulumi/libp2p";

const page = new libp2p.StaticPage("page", {
    indexContent: "<html><body><p>Hello world!</p></body></html>",
});

export const bucket = page.bucket;
export const url = page.websiteUrl;
