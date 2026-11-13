# 00aede2c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aede2c",
  "name": "FUN_00aede2c",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a5e8e51a17543eb273a68234f16144bcf6f1736925b1adc7dc0d4b06f7b4f165",
  "source_text_sha256": "a5e8e51a17543eb273a68234f16144bcf6f1736925b1adc7dc0d4b06f7b4f165"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)

## 疑似コード / UTF-8 321 bytes

~~~c

void FUN_00aede2c(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00aede38 to 00bededf has its CatchHandler @ 00aedb90 */
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c8dd38;
  puVar1[1] = uVar2;
  return;
}

~~~
