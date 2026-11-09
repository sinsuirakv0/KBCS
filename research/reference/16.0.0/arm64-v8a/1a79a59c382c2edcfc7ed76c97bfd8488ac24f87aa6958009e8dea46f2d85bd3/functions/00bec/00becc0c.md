# 00becc0c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00becc0c",
  "name": "FUN_00becc0c",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "32e73aa78f1966670805fb8aea062d6b5e59a2b1c7f8f9ff23dfd9b6e3368436",
  "source_text_sha256": "32e73aa78f1966670805fb8aea062d6b5e59a2b1c7f8f9ff23dfd9b6e3368436"
}
~~~

## 呼び出し元

- [00be5eb8](../00be5/00be5eb8.md)
- [00bec96c](../00bec/00bec96c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1877 bytes

~~~c

void FUN_00becc0c(ulong *param_1,ulong *param_2,ulong *param_3,ulong *param_4,ulong *param_5)

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
    }
    else {
      *param_1 = uVar1;
      *param_2 = uVar2;
      uVar3 = *param_3;
      if (uVar2 <= uVar3) goto LAB_00becc8c;
      *param_2 = uVar3;
    }
                    /* try { // try from 00becc80 to 00cecc8b has its CatchHandler @ 00bece88 */
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
LAB_00becc8c:
  if (*param_4 < uVar3) {
    *param_3 = *param_4;
    *param_4 = uVar3;
    uVar3 = *param_2;
    if (*param_3 < uVar3) {
      *param_2 = *param_3;
                    /* try { // try from 00beccb4 to 00ceccbf has its CatchHandler @ 00bece78 */
      *param_3 = uVar3;
      uVar3 = *param_1;
                    /* try { // try from 00beccc0 to 00ceccdb has its CatchHandler @ 00bece98 */
      if (*param_2 < uVar3) {
        *param_1 = *param_2;
        *param_2 = uVar3;
      }
    }
  }
  uVar3 = *param_4;
                    /* try { // try from 00beccdc to 00cecf17 has its CatchHandler @ 00bec538 */
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
