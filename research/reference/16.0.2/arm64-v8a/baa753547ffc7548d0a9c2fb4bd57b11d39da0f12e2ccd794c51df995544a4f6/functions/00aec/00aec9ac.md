# 00aec9ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aec9ac",
  "name": "FUN_00aec9ac",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2082b525469a91b690cedfde74da6dcf684d336738dfa5483f80fb422b896541",
  "source_text_sha256": "2082b525469a91b690cedfde74da6dcf684d336738dfa5483f80fb422b896541"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)

## 疑似コード / UTF-8 657 bytes

~~~c

void FUN_00aec9ac(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00aec9b0 to 00bec9f7 has its CatchHandler @ 00aec9b0
                       catch() { ... } // from try @ 00aec9b0 with catch @ 00aec9b0
                       catch() { ... } // from try @ 00aecaf8 with catch @ 00aec9b0
                       catch() { ... } // from try @ 00aecc8c with catch @ 00aec9b0
                       catch() { ... } // from try @ 00aecdcc with catch @ 00aec9b0 */
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c8dac8;
  puVar1[1] = uVar2;
  return;
}

~~~
