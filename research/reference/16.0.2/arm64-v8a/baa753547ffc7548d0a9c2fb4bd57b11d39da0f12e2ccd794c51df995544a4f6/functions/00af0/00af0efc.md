# 00af0efc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00af0efc",
  "name": "FUN_00af0efc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2485bf30a29fc0a78ee701d76d8cc567e8e181bf88db7ba7931bb21a42527604",
  "source_text_sha256": "2485bf30a29fc0a78ee701d76d8cc567e8e181bf88db7ba7931bb21a42527604"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)

## 疑似コード / UTF-8 321 bytes

~~~c

void FUN_00af0efc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00af0f04 to 00bf0f47 has its CatchHandler @ 00af1050 */
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c8e7c8;
  puVar1[1] = uVar2;
  return;
}

~~~
