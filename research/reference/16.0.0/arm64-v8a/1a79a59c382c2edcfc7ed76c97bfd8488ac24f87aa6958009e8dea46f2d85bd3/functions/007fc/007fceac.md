# 007fceac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "007fceac",
  "name": "FUN_007fceac",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "766514b7686b8919b02b6d57988873f388dfc5a26bd19a1cb11f446d5204f69d",
  "source_text_sha256": "766514b7686b8919b02b6d57988873f388dfc5a26bd19a1cb11f446d5204f69d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [007efc68](../007ef/007efc68.md)
- [008b9134](../008b9/008b9134.md)

## 疑似コード / UTF-8 471 bytes

~~~c

void FUN_007fceac(long param_1,undefined8 *param_2,int *param_3,uint *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  if (*param_3 == 2) {
    if (*param_4 < 2) {
      uVar2 = *param_2;
      uVar1 = FUN_0047acb4();
      FUN_0047cd94(uVar1,0xb,0);
      FUN_008b9134(uVar2);
      return;
    }
  }
  else if ((*param_3 == 5) && (*param_4 == 0)) {
    FUN_007efc68(*(undefined8 *)(param_1 + 8),*(undefined4 *)(param_1 + 0x10),0);
    return;
  }
  return;
}

~~~
