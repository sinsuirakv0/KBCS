# 00beebbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00beebbc",
  "name": "FUN_00beebbc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "89d7d7b673f5c4ec03773ce4de799b86546055e615f2290bd3bd2ce20989c66a",
  "source_text_sha256": "89d7d7b673f5c4ec03773ce4de799b86546055e615f2290bd3bd2ce20989c66a"
}
~~~

## 呼び出し元

- [00be7fdc](../00be7/00be7fdc.md)
- [00bee91c](../00bee/00bee91c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1529 bytes

~~~c

void FUN_00beebbc(double *param_1,double *param_2,double *param_3,double *param_4,double *param_5)

{
  double dVar1;
  double dVar2;
  double dVar3;
  
  dVar1 = *param_2;
  dVar2 = *param_1;
  dVar3 = *param_3;
  if (dVar2 <= dVar1) {
    if (dVar3 < dVar1) {
      *param_2 = dVar3;
      *param_3 = dVar1;
      dVar2 = *param_1;
      dVar3 = dVar1;
      if (*param_2 < dVar2) {
        *param_1 = *param_2;
        *param_2 = dVar2;
        dVar3 = *param_3;
      }
    }
  }
  else {
    if (dVar1 <= dVar3) {
      *param_1 = dVar1;
      *param_2 = dVar2;
      dVar3 = *param_3;
      if (dVar2 <= dVar3) goto LAB_00beec3c;
      *param_2 = dVar3;
    }
    else {
      *param_1 = dVar3;
    }
    *param_3 = dVar2;
    dVar3 = dVar2;
  }
LAB_00beec3c:
  if (*param_4 < dVar3) {
    *param_3 = *param_4;
    *param_4 = dVar3;
    dVar3 = *param_2;
    if (*param_3 < dVar3) {
      *param_2 = *param_3;
      *param_3 = dVar3;
      dVar3 = *param_1;
      if (*param_2 < dVar3) {
        *param_1 = *param_2;
        *param_2 = dVar3;
      }
    }
  }
  dVar3 = *param_4;
  if (*param_5 < dVar3) {
    *param_4 = *param_5;
    *param_5 = dVar3;
    dVar3 = *param_3;
    if (*param_4 < dVar3) {
      *param_3 = *param_4;
      *param_4 = dVar3;
      dVar3 = *param_2;
      if (*param_3 < dVar3) {
        *param_2 = *param_3;
        *param_3 = dVar3;
        dVar3 = *param_1;
        if (*param_2 < dVar3) {
          *param_1 = *param_2;
          *param_2 = dVar3;
        }
      }
    }
  }
  return;
}

~~~
