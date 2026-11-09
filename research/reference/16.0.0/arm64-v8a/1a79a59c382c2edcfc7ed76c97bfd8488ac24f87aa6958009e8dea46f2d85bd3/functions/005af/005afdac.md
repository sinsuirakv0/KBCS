# 005afdac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "005afdac",
  "name": "FUN_005afdac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b626c87be87a169afa6794e450f8b168ca8106dd384550259414c3273e488ed9",
  "source_text_sha256": "b626c87be87a169afa6794e450f8b168ca8106dd384550259414c3273e488ed9"
}
~~~

## 呼び出し元

- [00a47d08](../00a47/00a47d08.md)

## 呼び出し先

- [005afc38](../005af/005afc38.md)

## 疑似コード / UTF-8 190 bytes

~~~c

int FUN_005afdac(void)

{
  int iVar1;
  
  iVar1 = FUN_005afc38(2);
                    /* try { // try from 005afdc0 to 006afdcf has its CatchHandler @ 005b028c */
  return iVar1 + 3;
}

~~~
