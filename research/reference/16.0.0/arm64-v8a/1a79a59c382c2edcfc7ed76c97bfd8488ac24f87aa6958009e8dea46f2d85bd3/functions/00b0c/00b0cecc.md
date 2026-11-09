# 00b0cecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b0cecc",
  "name": "FUN_00b0cecc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "256583e0ab5f7d7f2cb539fca4fe436018423e7245de8effc70dba737a675b76",
  "source_text_sha256": "256583e0ab5f7d7f2cb539fca4fe436018423e7245de8effc70dba737a675b76"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008514b8](../00851/008514b8.md)
- [008b6a18](../008b6/008b6a18.md)
- [008b7984](../008b7/008b7984.md)

## 疑似コード / UTF-8 272 bytes

~~~c

void FUN_00b0cecc(void)

{
  long lVar1;
  undefined8 uVar2;
  
  lVar1 = FUN_008514b8();
  uVar2 = FUN_008b7984(lVar1 + 0x2f38,0x329);
  FUN_008b6a18(uVar2,0);
  lVar1 = FUN_008514b8();
  uVar2 = FUN_008b7984(lVar1 + 0x2f38,0x32a);
  FUN_008b6a18(uVar2,0);
  return;
}

~~~
