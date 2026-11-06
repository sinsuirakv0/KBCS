# 00bdae8c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bdae8c.md)

## 関数情報

~~~json
{
  "address": "00bdae8c",
  "name": "FUN_00bdae8c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28fdd512719092cd3b2fd72af488d8520641d13e58579793d34f5e45681f8c0c",
  "source_text_sha256": "28fdd512719092cd3b2fd72af488d8520641d13e58579793d34f5e45681f8c0c"
}
~~~
## 呼び出し元

- [009613bc](../00961/009613bc.md)

## 呼び出し先

- [00963004](../00963/00963004.md)

## 疑似コード 1/1 / UTF-8 146 bytes

~~~c

void FUN_00bdae8c(void)

{
                    /* catch() { ... } // from try @ 00bdae00 with catch @ 00bdae90 */
  FUN_00963004();
  return;
}

~~~
