# 00afaba4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afaba4",
  "name": "FUN_00afaba4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "89feba2e282f0e7f67f1ef5c5a4856b336479560e278e0434deaa67ec0bb8f81",
  "source_text_sha256": "89feba2e282f0e7f67f1ef5c5a4856b336479560e278e0434deaa67ec0bb8f81"
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 978 bytes

~~~c

void FUN_00afaba4(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
                    /* try { // try from 00afabcc to 00bfac67 has its CatchHandler @ 00afabcc
                       catch() { ... } // from try @ 00afabcc with catch @ 00afabcc
                       catch() { ... } // from try @ 00afac80 with catch @ 00afabcc
                       catch() { ... } // from try @ 00afad40 with catch @ 00afabcc
                       catch() { ... } // from try @ 00afae0c with catch @ 00afabcc
                       catch() { ... } // from try @ 00afafa8 with catch @ 00afabcc
                       catch() { ... } // from try @ 00afaff8 with catch @ 00afabcc
                       catch() { ... } // from try @ 00afb0a4 with catch @ 00afabcc
                       catch() { ... } // from try @ 00afb180 with catch @ 00afabcc */
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a28) = param_3 & 1;
  return;
}

~~~
