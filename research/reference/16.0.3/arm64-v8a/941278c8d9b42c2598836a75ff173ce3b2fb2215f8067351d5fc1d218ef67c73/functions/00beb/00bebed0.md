# 00bebed0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bebed0",
  "name": "FUN_00bebed0",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e38afad6af44b1a5a8f93df770fb865948d7b2dc8ad3fc9602ca750160b57a94",
  "source_text_sha256": "e38afad6af44b1a5a8f93df770fb865948d7b2dc8ad3fc9602ca750160b57a94"
}
~~~

## 呼び出し元

- [00be4fb0](../00be4/00be4fb0.md)
- [00bebc10](../00beb/00bebc10.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1767 bytes

~~~c

void FUN_00bebed0(short *param_1,short *param_2,short *param_3,short *param_4,short *param_5)

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
      if (sVar2 <= sVar3) goto LAB_00bebf50;
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
LAB_00bebf50:
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
                    /* try { // try from 00bebfe4 to 00cebfeb has its CatchHandler @ 00bebfec */
        if (*param_2 < sVar3) {
                    /* catch() { ... } // from try @ 00bebfe4 with catch @ 00bebfec
                       try { // try from 00bebfec to 00cec023 has its CatchHandler @ 00bebe80 */
          *param_1 = *param_2;
          *param_2 = sVar3;
        }
      }
    }
  }
  return;
}

~~~
