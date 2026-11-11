# 00aadfa4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aadfa4",
  "name": "FUN_00aadfa4",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "034249418f4bb5b367a1236c52634b97c926cad6e51e4ddc1b5caa7ca17c86e5",
  "source_text_sha256": "034249418f4bb5b367a1236c52634b97c926cad6e51e4ddc1b5caa7ca17c86e5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)

## 疑似コード / UTF-8 894 bytes

~~~c

void FUN_00aadfa4(long param_1)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  
  pbVar2 = *(byte **)(param_1 + 8);
  if (pbVar2 == (byte *)0x0) {
    return;
  }
  pbVar1 = *(byte **)(param_1 + 0x10);
  pbVar3 = pbVar2;
  if (pbVar1 != pbVar2) {
    do {
                    /* catch() { ... } // from try @ 00aadf38 with catch @ 00aadfe4 */
      pbVar3 = pbVar1 + -0x18;
      if ((*pbVar3 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar1 + -8));
      }
      pbVar1 = pbVar3;
    } while (pbVar3 != pbVar2);
    pbVar3 = *(byte **)(param_1 + 8);
  }
  *(byte **)(param_1 + 0x10) = pbVar2;
                    /* try { // try from 00aae00c to 00bae05b has its CatchHandler @ 00aae00c
                       catch() { ... } // from try @ 00aae00c with catch @ 00aae00c
                       catch() { ... } // from try @ 00aae064 with catch @ 00aae00c */
  _ZdlPv(pbVar3);
  return;
}

~~~
