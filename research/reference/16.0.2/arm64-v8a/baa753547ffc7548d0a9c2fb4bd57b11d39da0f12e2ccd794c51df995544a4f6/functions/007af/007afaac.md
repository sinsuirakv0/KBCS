# 007afaac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "007afaac",
  "name": "FUN_007afaac",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "db8ba7870a5ddb9145b5c0446aeeb519e04ebb0b2630c5815379806e885a79e5",
  "source_text_sha256": "db8ba7870a5ddb9145b5c0446aeeb519e04ebb0b2630c5815379806e885a79e5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_007afaac(undefined8 *param_1)

{
  long *plVar1;
  long *plVar2;
  long lVar3;
  
  plVar1 = (long *)param_1[6];
  plVar2 = param_1 + 2;
  *param_1 = &PTR_FUN_00c7aa68;
  if (plVar1 == plVar2) {
    lVar3 = 0x20;
  }
  else {
    if (plVar1 == (long *)0x0) goto LAB_007afaf8;
    lVar3 = 0x28;
    plVar2 = plVar1;
  }
  (**(code **)(*plVar2 + lVar3))();
LAB_007afaf8:
  _ZdlPv(param_1);
  return;
}

~~~
