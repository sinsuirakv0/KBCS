# 00be1cfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00be1cfc",
  "name": "_ZN8firebase4auth17UserInfoInterfaceD2Ev",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "94843f119f6eba4cbf94e4badf54b64940161807c39c6338456ff5e6ecbe1f7f",
  "source_text_sha256": "94843f119f6eba4cbf94e4badf54b64940161807c39c6338456ff5e6ecbe1f7f"
}
~~~

## 呼び出し元

- [00c5d770](../00c5d/00c5d770.md)
- [00c5d780](../00c5d/00c5d780.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 1019 bytes

~~~c

void _ZN8firebase4auth17UserInfoInterfaceD2Ev(long *param_1)

{
  byte bVar1;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth17UserInfoInterfaceE_00c9b5c8 + 0x10);
  if ((*(byte *)(param_1 + 0x10) & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 0xd);
  }
  else {
    _ZdlPv((void *)param_1[0x12]);
    bVar1 = *(byte *)(param_1 + 0xd);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 10);
  }
  else {
    _ZdlPv((void *)param_1[0xf]);
    bVar1 = *(byte *)(param_1 + 10);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 7);
  }
  else {
    _ZdlPv((void *)param_1[0xc]);
    bVar1 = *(byte *)(param_1 + 7);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 4);
  }
  else {
    _ZdlPv((void *)param_1[9]);
    bVar1 = *(byte *)(param_1 + 4);
  }
  if ((bVar1 & 1) == 0) {
    bVar1 = *(byte *)(param_1 + 1);
  }
  else {
    _ZdlPv((void *)param_1[6]);
    bVar1 = *(byte *)(param_1 + 1);
  }
  if ((bVar1 & 1) != 0) {
    _ZdlPv((void *)param_1[3]);
    return;
  }
  return;
}

~~~
