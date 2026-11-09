# 00beb0fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00beb0fc",
  "name": "FUN_00beb0fc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8dd1ba89603590d17eb6dfdce1882ed806fc982d23a33e0ed1fbf7bfa9033a3e",
  "source_text_sha256": "8dd1ba89603590d17eb6dfdce1882ed806fc982d23a33e0ed1fbf7bfa9033a3e"
}
~~~

## 呼び出し元

- [00be4234](../00be4/00be4234.md)
- [00beae3c](../00bea/00beae3c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1497 bytes

~~~c

void FUN_00beb0fc(ushort *param_1,ushort *param_2,ushort *param_3,ushort *param_4,ushort *param_5)

{
  ushort uVar1;
  ushort uVar2;
  ushort uVar3;
  
  uVar1 = *param_2;
  uVar2 = *param_1;
  uVar3 = *param_3;
  if (uVar1 < uVar2) {
    if (uVar3 < uVar1) {
      *param_1 = uVar3;
    }
    else {
      *param_1 = uVar1;
      *param_2 = uVar2;
      uVar3 = *param_3;
      if (uVar2 <= uVar3) goto LAB_00beb17c;
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
LAB_00beb17c:
  if (*param_4 < uVar3) {
    *param_3 = *param_4;
    *param_4 = uVar3;
    uVar1 = *param_2;
    if (*param_3 < uVar1) {
      *param_2 = *param_3;
      *param_3 = uVar1;
      uVar1 = *param_1;
      if (*param_2 < uVar1) {
        *param_1 = *param_2;
        *param_2 = uVar1;
      }
    }
  }
  uVar1 = *param_4;
  if (*param_5 < uVar1) {
    *param_4 = *param_5;
    *param_5 = uVar1;
    uVar1 = *param_3;
    if (*param_4 < uVar1) {
      *param_3 = *param_4;
      *param_4 = uVar1;
      uVar1 = *param_2;
      if (*param_3 < uVar1) {
        *param_2 = *param_3;
        *param_3 = uVar1;
        uVar1 = *param_1;
        if (*param_2 < uVar1) {
          *param_1 = *param_2;
          *param_2 = uVar1;
        }
      }
    }
  }
  return;
}

~~~
