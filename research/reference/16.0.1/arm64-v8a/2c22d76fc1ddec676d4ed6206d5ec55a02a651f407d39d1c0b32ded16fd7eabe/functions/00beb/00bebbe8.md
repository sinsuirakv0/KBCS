# 00bebbe8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bebbe8",
  "name": "FUN_00bebbe8",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "59b0fc1e84d11440dd12a50dadd1a0c752499829c9f1d05bad1e0ba26bc45f53",
  "source_text_sha256": "59b0fc1e84d11440dd12a50dadd1a0c752499829c9f1d05bad1e0ba26bc45f53"
}
~~~

## 呼び出し元

- [00be4d98](../00be4/00be4d98.md)
- [00beb948](../00beb/00beb948.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1473 bytes

~~~c

void FUN_00bebbe8(int *param_1,int *param_2,int *param_3,int *param_4,int *param_5)

{
  int iVar1;
  int iVar2;
  int iVar3;
  
  iVar1 = *param_2;
  iVar2 = *param_1;
  iVar3 = *param_3;
  if (iVar1 < iVar2) {
    if (iVar3 < iVar1) {
      *param_1 = iVar3;
    }
    else {
      *param_1 = iVar1;
      *param_2 = iVar2;
      iVar3 = *param_3;
      if (iVar2 <= iVar3) goto LAB_00bebc68;
      *param_2 = iVar3;
    }
    *param_3 = iVar2;
    iVar3 = iVar2;
  }
  else if (iVar3 < iVar1) {
    *param_2 = iVar3;
    *param_3 = iVar1;
    iVar2 = *param_1;
    iVar3 = iVar1;
    if (*param_2 < iVar2) {
      *param_1 = *param_2;
      *param_2 = iVar2;
      iVar3 = *param_3;
    }
  }
LAB_00bebc68:
  if (*param_4 < iVar3) {
    *param_3 = *param_4;
    *param_4 = iVar3;
    iVar1 = *param_2;
    if (*param_3 < iVar1) {
      *param_2 = *param_3;
      *param_3 = iVar1;
      iVar1 = *param_1;
      if (*param_2 < iVar1) {
        *param_1 = *param_2;
        *param_2 = iVar1;
      }
    }
  }
  iVar1 = *param_4;
  if (*param_5 < iVar1) {
    *param_4 = *param_5;
    *param_5 = iVar1;
    iVar1 = *param_3;
    if (*param_4 < iVar1) {
      *param_3 = *param_4;
      *param_4 = iVar1;
      iVar1 = *param_2;
      if (*param_3 < iVar1) {
        *param_2 = *param_3;
        *param_3 = iVar1;
        iVar1 = *param_1;
        if (*param_2 < iVar1) {
          *param_1 = *param_2;
          *param_2 = iVar1;
        }
      }
    }
  }
  return;
}

~~~
