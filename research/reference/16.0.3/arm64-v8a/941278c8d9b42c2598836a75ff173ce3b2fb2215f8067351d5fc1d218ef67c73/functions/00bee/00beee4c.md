# 00beee4c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00beee4c",
  "name": "FUN_00beee4c",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e9ef1dff563ca7edf5e4e7825493857b5bb548a3f8dd8fd5d973de2a20d2da2",
  "source_text_sha256": "9e9ef1dff563ca7edf5e4e7825493857b5bb548a3f8dd8fd5d973de2a20d2da2"
}
~~~

## 呼び出し元

- [00be81a0](../00be8/00be81a0.md)
- [00beebac](../00bee/00beebac.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 2090 bytes

~~~c

void FUN_00beee4c(ulong *param_1,ulong *param_2,ulong *param_3,ulong *param_4,ulong *param_5)

{
  ulong uVar1;
  ulong uVar2;
  ulong uVar3;
  
  uVar1 = *param_2;
  uVar2 = *param_1;
  uVar3 = *param_3;
  if (uVar1 < uVar2) {
    if (uVar3 < uVar1) {
      *param_1 = uVar3;
                    /* try { // try from 00beee70 to 00ceefcb has its CatchHandler @ 00beee70
                       catch() { ... } // from try @ 00beee70 with catch @ 00beee70
                       catch() { ... } // from try @ 00bef018 with catch @ 00beee70
                       catch() { ... } // from try @ 00bef0f4 with catch @ 00beee70
                       catch() { ... } // from try @ 00bef1c0 with catch @ 00beee70
                       catch() { ... } // from try @ 00bef2e8 with catch @ 00beee70
                       catch() { ... } // from try @ 00bef54c with catch @ 00beee70 */
    }
    else {
      *param_1 = uVar1;
      *param_2 = uVar2;
      uVar3 = *param_3;
      if (uVar2 <= uVar3) goto LAB_00beeecc;
      *param_2 = uVar3;
    }
    *param_3 = uVar2;
    uVar3 = uVar2;
  }
  else if (uVar3 < uVar1) {
    *param_2 = uVar3;
    *param_3 = uVar1;
    uVar2 = *param_1;
    uVar3 = uVar1;
    if (*param_2 < uVar2) {
      *param_1 = *param_2;
      *param_2 = uVar2;
      uVar3 = *param_3;
    }
  }
LAB_00beeecc:
  if (*param_4 < uVar3) {
    *param_3 = *param_4;
    *param_4 = uVar3;
    uVar3 = *param_2;
    if (*param_3 < uVar3) {
      *param_2 = *param_3;
      *param_3 = uVar3;
      uVar3 = *param_1;
      if (*param_2 < uVar3) {
        *param_1 = *param_2;
        *param_2 = uVar3;
      }
    }
  }
  uVar3 = *param_4;
  if (*param_5 < uVar3) {
    *param_4 = *param_5;
    *param_5 = uVar3;
    uVar3 = *param_3;
    if (*param_4 < uVar3) {
      *param_3 = *param_4;
      *param_4 = uVar3;
      uVar3 = *param_2;
      if (*param_3 < uVar3) {
        *param_2 = *param_3;
        *param_3 = uVar3;
        uVar3 = *param_1;
        if (*param_2 < uVar3) {
          *param_1 = *param_2;
          *param_2 = uVar3;
        }
      }
    }
  }
  return;
}

~~~
