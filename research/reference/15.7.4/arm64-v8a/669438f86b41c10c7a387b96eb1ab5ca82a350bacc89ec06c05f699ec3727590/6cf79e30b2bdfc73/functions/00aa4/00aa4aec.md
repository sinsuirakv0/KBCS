# 00aa4aec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aa4aec.md)

## 関数情報

~~~json
{
  "address": "00aa4aec",
  "name": "FUN_00aa4aec",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f0649215b830093f9f5ea50c77ec6617883d0c56393cbfb98a60f161fd58e860",
  "source_text_sha256": "f0649215b830093f9f5ea50c77ec6617883d0c56393cbfb98a60f161fd58e860"
}
~~~
## 呼び出し元

- [0069ef54](../0069e/0069ef54.md)
- [009f1ea8](../009f1/009f1ea8.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 467 bytes

~~~c

bool FUN_00aa4aec(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
                    /* try { // try from 00aa4af4 to 00ba4b4f has its CatchHandler @ 00aa59b4 */
  lVar2 = FUN_0081f580();
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar3 & 1) == 0) {
    lVar2 = FUN_0081f580();
    bVar1 = *(int *)(&uleb128_0023a2c4 + lVar2 + (long)param_2 * 0x1c4) != 0;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
