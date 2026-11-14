# 00befbb0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00befbb0",
  "name": "FUN_00befbb0",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "71c449da935a01c52233ffc56f432ef429393d2ca9fc55807b903566a57f1bfc",
  "source_text_sha256": "71c449da935a01c52233ffc56f432ef429393d2ca9fc55807b903566a57f1bfc"
}
~~~

## 呼び出し元

- [00be8fd0](../00be8/00be8fd0.md)
- [00bef910](../00bef/00bef910.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1529 bytes

~~~c

void FUN_00befbb0(double *param_1,double *param_2,double *param_3,double *param_4,double *param_5)

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
      if (dVar2 <= dVar3) goto LAB_00befc30;
      *param_2 = dVar3;
    }
    else {
      *param_1 = dVar3;
    }
    *param_3 = dVar2;
    dVar3 = dVar2;
  }
LAB_00befc30:
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
