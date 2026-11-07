# 00b5accc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00b5add8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5add8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00b5accc",
  "name": "_ZN8firebase4auth4Auth8FindAuthEPNS_3AppE",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "359950d82669be1a9c810298ac2454fecbcfa4871bc6cda80d3ddc82f917868f",
  "source_text_sha256": "359950d82669be1a9c810298ac2454fecbcfa4871bc6cda80d3ddc82f917868f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

## 疑似コード / UTF-8 1234 bytes

~~~c

undefined8 _ZN8firebase4auth4Auth8FindAuthEPNS_3AppE(ulong param_1)

{
  undefined *puVar1;
  undefined *puVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  
  uVar3 = *(undefined8 *)PTR__ZN8firebase4auth13g_auths_mutexE_00c1ba70;
                    /* try { // try from 00b5acec to 00c5acff has its CatchHandler @ 00b5ae88 */
  _ZN8firebase5Mutex7AcquireEv(uVar3);
  puVar2 = *(undefined **)(PTR__ZN8firebase4auth7g_authsE_00c1ba78 + 8);
  if (puVar2 != (undefined *)0x0) {
    puVar1 = PTR__ZN8firebase4auth7g_authsE_00c1ba78 + 8;
    do {
      if (*(ulong *)(puVar2 + 0x20) >= param_1) {
        puVar1 = puVar2;
      }
      puVar2 = *(undefined **)(puVar2 + (ulong)(*(ulong *)(puVar2 + 0x20) < param_1) * 8);
    } while (puVar2 != (undefined *)0x0);
    if ((puVar1 != PTR__ZN8firebase4auth7g_authsE_00c1ba78 + 8) &&
       (*(ulong *)(puVar1 + 0x20) <= param_1)) {
      uVar4 = *(undefined8 *)(puVar1 + 0x28);
      goto LAB_00b5ad38;
    }
  }
                    /* try { // try from 00b5ad34 to 00c5ad43 has its CatchHandler @ 00b5aea4 */
  uVar4 = 0;
LAB_00b5ad38:
  _ZN8firebase5Mutex7ReleaseEv(uVar3);
                    /* try { // try from 00b5ad44 to 00c5ad57 has its CatchHandler @ 00b5ae8c */
  return uVar4;
}

~~~
