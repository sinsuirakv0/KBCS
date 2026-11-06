# 00a4fdbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00a4fdbc",
  "name": "FUN_00a4fdbc",
  "size": 268,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28b563a30ccddac7ac82ec642e771b0a38a5e851b6c57f30ab7467f93bd983e3",
  "source_text_sha256": "28b563a30ccddac7ac82ec642e771b0a38a5e851b6c57f30ab7467f93bd983e3"
}
~~~

## 呼び出し元

- [00a4b1c8](../00a4b/00a4b1c8.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード / UTF-8 1380 bytes

~~~c

void FUN_00a4fdbc(byte *param_1)

{
  byte bVar1;
  
  if ((param_1[0xd8] & 1) == 0) {
    bVar1 = param_1[0xc0];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0xe8));
    bVar1 = param_1[0xc0];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0xa8];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0xd0));
    bVar1 = param_1[0xa8];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x90];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0xb8));
    bVar1 = param_1[0x90];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x78];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0xa0));
    bVar1 = param_1[0x78];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x60];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x88));
    bVar1 = param_1[0x60];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x48];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x70));
    bVar1 = param_1[0x48];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x30];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x58));
    bVar1 = param_1[0x30];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x18];
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x40));
    bVar1 = param_1[0x18];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *param_1;
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x28));
    bVar1 = *param_1;
  }
  if ((bVar1 & 1) != 0) {
    _ZdlPv(*(void **)(param_1 + 0x10));
    return;
  }
  return;
}

~~~
