# 005afdec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "005afdec",
  "name": "FUN_005afdec",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bb90ce07b03258c02c1003fd5fb0d3e8f527eda4e069f18f284966c44101f007",
  "source_text_sha256": "bb90ce07b03258c02c1003fd5fb0d3e8f527eda4e069f18f284966c44101f007"
}
~~~

## 呼び出し元

- [00a47f00](../00a47/00a47f00.md)

## 呼び出し先

- [005afc78](../005af/005afc78.md)

## 疑似コード / UTF-8 190 bytes

~~~c

int FUN_005afdec(void)

{
  int iVar1;
  
  iVar1 = FUN_005afc78(2);
                    /* try { // try from 005afe00 to 006afe0f has its CatchHandler @ 005b02cc */
  return iVar1 + 3;
}

~~~
