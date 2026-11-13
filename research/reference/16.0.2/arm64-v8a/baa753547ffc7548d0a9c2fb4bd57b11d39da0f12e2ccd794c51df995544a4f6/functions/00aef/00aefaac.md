# 00aefaac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aefaac",
  "name": "FUN_00aefaac",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "65ea570066b760adaec21e44a4046e330b0988658cadc69f7b683da38a1e820f",
  "source_text_sha256": "65ea570066b760adaec21e44a4046e330b0988658cadc69f7b683da38a1e820f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 283 bytes

~~~c

void FUN_00aefaac(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
                    /* try { // try from 00aefaac to 00befb1b has its CatchHandler @ 00aef934 */
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c8e1b8;
  param_2[1] = uVar1;
  return;
}

~~~
