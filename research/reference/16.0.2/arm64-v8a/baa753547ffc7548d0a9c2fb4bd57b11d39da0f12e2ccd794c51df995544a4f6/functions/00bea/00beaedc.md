# 00beaedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00beaedc",
  "name": "FUN_00beaedc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c45a72cf2ffda3dadceac383fe92453732998a122c9f231fa1e67a16bf9d6912",
  "source_text_sha256": "c45a72cf2ffda3dadceac383fe92453732998a122c9f231fa1e67a16bf9d6912"
}
~~~

## 呼び出し元

- [00be3fbc](../00be3/00be3fbc.md)
- [00beac1c](../00bea/00beac1c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1767 bytes

~~~c

void FUN_00beaedc(short *param_1,short *param_2,short *param_3,short *param_4,short *param_5)

{
  short sVar1;
  short sVar2;
  short sVar3;
  
  sVar1 = *param_2;
  sVar2 = *param_1;
  sVar3 = *param_3;
  if (sVar1 < sVar2) {
    if (sVar3 < sVar1) {
      *param_1 = sVar3;
    }
    else {
      *param_1 = sVar1;
      *param_2 = sVar2;
      sVar3 = *param_3;
      if (sVar2 <= sVar3) goto LAB_00beaf5c;
      *param_2 = sVar3;
    }
    *param_3 = sVar2;
    sVar3 = sVar2;
  }
  else if (sVar3 < sVar1) {
    *param_2 = sVar3;
    *param_3 = sVar1;
    sVar2 = *param_1;
    sVar3 = sVar1;
    if (*param_2 < sVar2) {
      *param_1 = *param_2;
      *param_2 = sVar2;
      sVar3 = *param_3;
    }
  }
LAB_00beaf5c:
  if (*param_4 < sVar3) {
    *param_3 = *param_4;
    *param_4 = sVar3;
    sVar3 = *param_2;
    if (*param_3 < sVar3) {
      *param_2 = *param_3;
      *param_3 = sVar3;
      sVar3 = *param_1;
      if (*param_2 < sVar3) {
        *param_1 = *param_2;
        *param_2 = sVar3;
      }
    }
  }
  sVar3 = *param_4;
  if (*param_5 < sVar3) {
    *param_4 = *param_5;
    *param_5 = sVar3;
    sVar3 = *param_3;
    if (*param_4 < sVar3) {
      *param_3 = *param_4;
      *param_4 = sVar3;
      sVar3 = *param_2;
      if (*param_3 < sVar3) {
        *param_2 = *param_3;
        *param_3 = sVar3;
        sVar3 = *param_1;
                    /* try { // try from 00beaff0 to 00ceaff7 has its CatchHandler @ 00beaff8 */
        if (*param_2 < sVar3) {
                    /* catch() { ... } // from try @ 00beaff0 with catch @ 00beaff8
                       try { // try from 00beaff8 to 00ceb02f has its CatchHandler @ 00beae8c */
          *param_1 = *param_2;
          *param_2 = sVar3;
        }
      }
    }
  }
  return;
}

~~~
