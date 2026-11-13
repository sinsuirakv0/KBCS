# 00afadfc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afadfc",
  "name": "FUN_00afadfc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45e94d8801fdc532f7fcb50e322f6a3c25f7b3173d27b3db61498d1debdeccb4",
  "source_text_sha256": "45e94d8801fdc532f7fcb50e322f6a3c25f7b3173d27b3db61498d1debdeccb4"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 306 bytes

~~~c

void FUN_00afadfc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
                    /* try { // try from 00afae14 to 00bfae5f has its CatchHandler @ 00afb440 */
  lVar1 = FUN_00851550();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a34) = param_3 & 1;
  return;
}

~~~
