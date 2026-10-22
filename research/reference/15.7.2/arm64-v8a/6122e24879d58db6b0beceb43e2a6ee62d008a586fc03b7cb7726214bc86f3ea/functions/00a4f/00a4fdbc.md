# 00a4fdbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a4fdbc.md)

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
  "source_sha256": "757d2342a9c92467bcf31b8966d27758842e878482e35f40ee8febe6f6568b5f",
  "source_text_sha256": "757d2342a9c92467bcf31b8966d27758842e878482e35f40ee8febe6f6568b5f"
}
~~~
## 呼び出し元

- [00a4b1c8](../00a4b/00a4b1c8.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード 1/1 / UTF-8 1546 bytes

~~~c

void FUN_00a4fdbc(byte *param_1)

{
  byte bVar1;
  
  if ((param_1[0xd8] & 1) == 0) {
    bVar1 = param_1[0xc0];
  }
  else {
    operator_delete(*(void **)(param_1 + 0xe8));
    bVar1 = param_1[0xc0];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0xa8];
  }
  else {
    operator_delete(*(void **)(param_1 + 0xd0));
    bVar1 = param_1[0xa8];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x90];
  }
  else {
    operator_delete(*(void **)(param_1 + 0xb8));
    bVar1 = param_1[0x90];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x78];
  }
  else {
    operator_delete(*(void **)(param_1 + 0xa0));
    bVar1 = param_1[0x78];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x60];
  }
  else {
    operator_delete(*(void **)(param_1 + 0x88));
    bVar1 = param_1[0x60];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x48];
  }
  else {
    operator_delete(*(void **)(param_1 + 0x70));
    bVar1 = param_1[0x48];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x30];
  }
  else {
    operator_delete(*(void **)(param_1 + 0x58));
    bVar1 = param_1[0x30];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = param_1[0x18];
  }
  else {
    operator_delete(*(void **)(param_1 + 0x40));
    bVar1 = param_1[0x18];
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *param_1;
  }
  else {
    operator_delete(*(void **)(param_1 + 0x28));
    bVar1 = *param_1;
  }
  if ((bVar1 & 1) != 0) {
    operator_delete(*(void **)(param_1 + 0x10));
    return;
  }
  return;
}

~~~
