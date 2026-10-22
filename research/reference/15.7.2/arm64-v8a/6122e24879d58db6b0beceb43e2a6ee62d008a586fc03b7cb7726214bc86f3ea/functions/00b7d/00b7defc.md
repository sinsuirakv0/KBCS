# 00b7defc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b7defc.md)

## 関数情報

~~~json
{
  "address": "00b7defc",
  "name": "FUN_00b7defc",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e8fc19a1c9129ed9078875fa453943cbce42d3bd80ef32044ef1cfd659918059",
  "source_text_sha256": "e8fc19a1c9129ed9078875fa453943cbce42d3bd80ef32044ef1cfd659918059"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00b7b694](../00b7b/00b7b694.md)
- [00bdaf40](../00bda/00bdaf40.md)

## 関連文字列（未確認候補）

~~~text
"unspecified iostream_category error"
~~~
## 疑似コード 1/1 / UTF-8 1093 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00b7defc(undefined8 *param_1,undefined8 param_2,int param_3)

{
  undefined8 uVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  char *pcVar7;
  
  if ((param_3 != 1) && (param_3 < 0x1000)) {
    FUN_00b7b694();
    return;
  }
  pcVar7 = operator_new(0x28);
  param_1[2] = pcVar7;
  uVar6 = _UNK_002b1018;
  uVar5 = _DAT_002b1010;
  uVar4 = s_unspecified_iostream_category_er_002ad6de._24_8_;
  uVar3 = s_unspecified_iostream_category_er_002ad6de._16_8_;
  uVar2 = s_unspecified_iostream_category_er_002ad6de._8_8_;
  uVar1 = s_unspecified_iostream_category_er_002ad6de._0_8_;
  pcVar7[0x1f] = 'r';
  pcVar7[0x20] = 'r';
  pcVar7[0x21] = 'o';
  pcVar7[0x22] = 'r';
  param_1[1] = uVar6;
  *param_1 = uVar5;
  *(undefined8 *)(pcVar7 + 8) = uVar2;
  *(undefined8 *)pcVar7 = uVar1;
  *(undefined8 *)(pcVar7 + 0x18) = uVar4;
  *(undefined8 *)(pcVar7 + 0x10) = uVar3;
  pcVar7[0x23] = '\0';
  return;
}

~~~
