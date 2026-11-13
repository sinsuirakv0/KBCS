# 00afdfb4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afdfb4",
  "name": "FUN_00afdfb4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23ef5809559f7d8ec4c67fe0ad0e2d3855d1ad7bf449a8e0d40d1cdd418a7e1a",
  "source_text_sha256": "23ef5809559f7d8ec4c67fe0ad0e2d3855d1ad7bf449a8e0d40d1cdd418a7e1a"
}
~~~

## 呼び出し元

- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00afdfb4(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c7c) = param_3;
  return;
}

~~~
