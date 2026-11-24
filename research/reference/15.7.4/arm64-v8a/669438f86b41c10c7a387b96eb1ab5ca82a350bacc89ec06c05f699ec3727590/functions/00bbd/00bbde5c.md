# 00bbde5c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbde18`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-0d436f25414b8a40f37ccc9d09eabc5d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0093.md#review-9d97c4d38bb43cc86978d7011d85514c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbde5c",
  "name": "FUN_00bbde5c",
  "size": 5016,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b767e72da1599fb1935953d11b4727c2b52e34ec85b07fcae82b79fe6657dfc7",
  "source_text_sha256": "b767e72da1599fb1935953d11b4727c2b52e34ec85b07fcae82b79fe6657dfc7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbde5c",
        "00bbf1f3"
      ]
    ],
    "bytes_sha256": "c358656dc3215b07eda14b6e9a24c5cdf1813463489a4bc53e51a24057f2e274",
    "instruction_count": 1254,
    "instruction_bytes": 5016,
    "body_bytes": 5016,
    "indirect": 2,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbcc10](../00bbc/00bbcc10.md)
- [00bbd308](../00bbd/00bbd308.md)
- [00bbde5c](../00bbd/00bbde5c.md)
- [00bbfad0](../00bbf/00bbfad0.md)
- [00bc2f0c](../00bc2/00bc2f0c.md)
- [00bc48e0](../00bc4/00bc48e0.md)
- [00bc5928](../00bc5/00bc5928.md)
- [00bc5b50](../00bc5/00bc5b50.md)
- [00bc6020](../00bc6/00bc6020.md)
- [00bc96b0](../00bc9/00bc96b0.md)
- [00bca9c4](../00bca/00bca9c4.md)
- [00bcecec](../00bce/00bcecec.md)
- [00bd11d0](../00bd1/00bd11d0.md)
- [00bd1778](../00bd1/00bd1778.md)
- [00bd1ff8](../00bd1/00bd1ff8.md)

## 呼び出し先

- [00bbdd1c](../00bbd/00bbdd1c.md)
- [00bbde5c](../00bbd/00bbde5c.md)
- [00bbf39c](../00bbf/00bbf39c.md)
- [00bbfdf8](../00bbf/00bbfdf8.md)
- [00bc136c](../00bc1/00bc136c.md)
- [00bc15e4](../00bc1/00bc15e4.md)
- [00bc1754](../00bc1/00bc1754.md)
- [00bc1c24](../00bc1/00bc1c24.md)
- [00bc1ccc](../00bc1/00bc1ccc.md)
- [00bc2090](../00bc2/00bc2090.md)
- [00bc2a60](../00bc2/00bc2a60.md)
- [00bc2bd8](../00bc2/00bc2bd8.md)
- [00bc2f0c](../00bc2/00bc2f0c.md)
- [00bc6374](../00bc6/00bc6374.md)
- [00bc9604](../00bc9/00bc9604.md)
- [00bd0280](../00bd0/00bd0280.md)
- [00bd11d0](../00bd1/00bd11d0.md)
- [00bd1778](../00bd1/00bd1778.md)
- [00bd1b50](../00bd1/00bd1b50.md)
- [00bd1bfc](../00bd1/00bd1bfc.md)
- [00bd1ca8](../00bd1/00bd1ca8.md)
- [00bd1d54](../00bd1/00bd1d54.md)
- [00bd1e00](../00bd1/00bd1e00.md)
- [00bd1ea0](../00bd1/00bd1ea0.md)
- [00bd1f4c](../00bd1/00bd1f4c.md)
- [00bd1ff8](../00bd1/00bd1ff8.md)
- [00bd22b4](../00bd2/00bd22b4.md)
- [00bd2404](../00bd2/00bd2404.md)
- [00bd24b0](../00bd2/00bd24b0.md)
- [00bd256c](../00bd2/00bd256c.md)
- [00bd261c](../00bd2/00bd261c.md)
- [00bd3d8c](../00bd3/00bd3d8c.md)
- [00bd4008](../00bd4/00bd4008.md)
- [00bdb0f0](../00bdb/00bdb0f0.md)
- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
" auto"
" decltype(auto)"
"__float128"
"__int128"
"auto"
"bool"
"char"
"char16_t"
"char32_t"
"char8_t"
"decimal128"
"decimal32"
"decimal64"
"decltype(auto)"
"double"
"half"
"long"
"long double"
"long long"
"short"
"std::nullptr_t"
"unsigned __int128"
"unsigned int"
"unsigned long"
"unsigned long long"
"unsigned short"
"void"
"wchar_t"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 43462 bytes

~~~c

undefined8 * FUN_00bbde5c(long *param_1)

{
  char cVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  void *pvVar4;
  ulong uVar5;
  byte *pbVar6;
  undefined *puVar7;
  char *pcVar8;
  ushort uVar9;
  long lVar10;
  undefined8 uVar11;
  char *pcVar12;
  byte *pbVar13;
  uint uVar14;
  ulong uVar15;
  ulong uVar16;
  long lVar17;
  size_t __n;
  long *__src;
  long *plVar18;
  undefined8 *local_58;
  undefined1 local_50 [16];
  ulong local_28;
  
  pcVar12 = (char *)*param_1;
  pbVar6 = (byte *)param_1[1];
  local_58 = (undefined8 *)0x0;
  uVar5 = (long)pbVar6 - (long)pcVar12;
  if (uVar5 == 0) goto code_r0x00bbe890;
  cVar1 = *pcVar12;
  switch(cVar1) {
  case 'A':
    pbVar13 = (byte *)(pcVar12 + 1);
    local_28 = 0;
                    /* try { // try from 00bbe4a8 to 00cbe4b3 has its CatchHandler @ 00bbeeb0 */
    *param_1 = (long)pbVar13;
    if (pbVar6 == pbVar13) {
LAB_00bbee08:
      uVar5 = FUN_00bc2f0c(param_1);
      puVar3 = (undefined8 *)0x0;
      if (uVar5 == 0) goto joined_r0x00bbef30;
                    /* try { // try from 00bbee14 to 00cbee1b has its CatchHandler @ 00bbef38 */
      pcVar12 = (char *)*param_1;
      if ((pcVar12 == (char *)param_1[1]) || (*pcVar12 != '_')) {
        return (undefined8 *)0x0;
      }
      pcVar12 = pcVar12 + 1;
      local_28 = uVar5;
                    /* try { // try from 00bbee30 to 00cbee37 has its CatchHandler @ 00bbef10 */
    }
    else {
                    /* try { // try from 00bbe4b4 to 00cbe4c3 has its CatchHandler @ 00bbee9c */
      if (*pbVar13 - 0x3a < 0xfffffff6) {
                    /* try { // try from 00bbe4c4 to 00cbe4d7 has its CatchHandler @ 00bbee84 */
        if (*pbVar13 != 0x5f) goto LAB_00bbee08;
        pcVar12 = pcVar12 + 2;
      }
      else {
        local_50 = FUN_00bbdd1c(param_1,0);
                    /* try { // try from 00bbee4c to 00cbee4f has its CatchHandler @ 00bbef38 */
                    /* catch() { ... } // from try @ 00bbe880 with catch @ 00bbee50
                       try { // try from 00bbee50 to 00cbefcb has its CatchHandler @ 00bbe1d0 */
        local_28 = FUN_00bc2a60(param_1,local_50);
                    /* catch() { ... } // from try @ 00bbe5f4 with catch @ 00bbee54 */
        pcVar12 = (char *)*param_1;
        if (pcVar12 == (char *)param_1[1]) {
          return (undefined8 *)0x0;
        }
                    /* catch() { ... } // from try @ 00bbe5e4 with catch @ 00bbee6c */
        if (*pcVar12 != '_') {
          return (undefined8 *)0x0;
        }
        pcVar12 = pcVar12 + 1;
      }
    }
    *param_1 = (long)pcVar12;
    pbVar6 = (byte *)FUN_00bbde5c(param_1);
                    /* catch() { ... } // from try @ 00bbe5d8 with catch @ 00bbee80 */
                    /* catch() { ... } // from try @ 00bbe4c4 with catch @ 00bbee84 */
    puVar3 = (undefined8 *)0x0;
    local_50._0_8_ = pbVar6;
    if (pbVar6 != (byte *)0x0) {
      puVar3 = (undefined8 *)FUN_00bd3d8c(param_1,local_50,&local_28);
    }
    goto joined_r0x00bbef30;
  default:
    goto code_r0x00bbe890;
  case 'C':
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00bbde5c(param_1);
    if ((byte *)local_50._0_8_ == (byte *)0x0) {
      return (undefined8 *)0x0;
    }
    puVar3 = (undefined8 *)FUN_00bd256c(param_1,local_50);
    goto LAB_00bbe89c;
  case 'D':
                    /* try { // try from 00bbe930 to 00cbe997 has its CatchHandler @ 00bbef84 */
    if (uVar5 < 2) {
      return (undefined8 *)0x0;
    }
    cVar1 = pcVar12[1];
    puVar2 = (undefined8 *)0x0;
    switch(cVar1) {
    case 'B':
    case 'U':
                    /* catch() { ... } // from try @ 00bbe3ec with catch @ 00bbef3c */
                    /* catch() { ... } // from try @ 00bbebc8 with catch @ 00bbef40 */
      pbVar13 = (byte *)(pcVar12 + 2);
                    /* catch() { ... } // from try @ 00bbe9e0 with catch @ 00bbef44 */
                    /* catch() { ... } // from try @ 00bbe468 with catch @ 00bbef48
                       catch() { ... } // from try @ 00bbe598 with catch @ 00bbef48
                       catch() { ... } // from try @ 00bbe7f0 with catch @ 00bbef48
                       catch() { ... } // from try @ 00bbeb0c with catch @ 00bbef48
                       catch() { ... } // from try @ 00bbec1c with catch @ 00bbef48 */
                    /* catch() { ... } // from try @ 00bbe8d8 with catch @ 00bbef4c
                       catch() { ... } // from try @ 00bbeae4 with catch @ 00bbef4c */
      *param_1 = (long)pbVar13;
                    /* catch() { ... } // from try @ 00bbedc8 with catch @ 00bbef50
                       catch() { ... } // from try @ 00bbedfc with catch @ 00bbef50 */
      local_28 = CONCAT71(local_28._1_7_,cVar1 == 'B');
                    /* catch() { ... } // from try @ 00bbe378 with catch @ 00bbef64 */
      if ((pbVar6 == pbVar13) || (*pbVar13 - 0x3a < 0xfffffff6)) {
                    /* catch() { ... } // from try @ 00bbe8b0 with catch @ 00bbef68 */
                    /* catch() { ... } // from try @ 00bbe568 with catch @ 00bbef6c */
        local_50._0_8_ = FUN_00bc2f0c(param_1);
                    /* catch() { ... } // from try @ 00bbe574 with catch @ 00bbef70 */
                    /* catch() { ... } // from try @ 00bbe368 with catch @ 00bbef74 */
        if (local_50._0_8_ == 0) {
          return (undefined8 *)0x0;
        }
      }
      else {
        local_50 = FUN_00bbdd1c(param_1,0);
        lVar10 = FUN_00bc2a60(param_1,local_50);
        local_50._0_8_ = lVar10;
      }
      pcVar12 = (char *)*param_1;
      if (pcVar12 == (char *)param_1[1]) {
        return (undefined8 *)0x0;
      }
                    /* try { // try from 00bbf1c4 to 00cbf1cb has its CatchHandler @ 00bbf514 */
      if (*pcVar12 != '_') {
        return (undefined8 *)0x0;
      }
      *param_1 = (long)(pcVar12 + 1);
      puVar3 = (undefined8 *)FUN_00bd1ea0(param_1,local_50,&local_28);
      return puVar3;
    default:
      goto code_r0x00bbed70;
    case 'F':
                    /* try { // try from 00bbf028 to 00cbf0bf has its CatchHandler @ 00bbf0c0 */
      *param_1 = (long)(pcVar12 + 2);
      local_50 = FUN_00bbdd1c(param_1,0);
      uVar11 = FUN_00bc2a60(param_1,local_50);
      pcVar12 = (char *)*param_1;
      if ((pcVar12 != (char *)param_1[1]) && (*pcVar12 == '_')) {
        *param_1 = (long)(pcVar12 + 1);
        local_50._0_8_ = uVar11;
        puVar3 = (undefined8 *)FUN_00bd1e00(param_1,local_50);
        return puVar3;
      }
      return (undefined8 *)0x0;
    case 'K':
    case 'k':
                    /* catch() { ... } // from try @ 00bbe2ac with catch @ 00bbeecc */
      local_50._0_8_ = " auto";
                    /* catch() { ... } // from try @ 00bbe2a0 with catch @ 00bbeee4 */
      if (cVar1 != 'k') {
        local_50._0_8_ = " decltype(auto)";
      }
      local_50._8_8_ = 5;
      if (cVar1 != 'k') {
        local_50._8_8_ = 0xf;
      }
      *param_1 = (long)(pcVar12 + 2);
      local_28 = FUN_00bbf39c(param_1,0);
                    /* catch() { ... } // from try @ 00bbe218 with catch @ 00bbef08 */
      if (local_28 != 0) {
                    /* catch() { ... } // from try @ 00bbee30 with catch @ 00bbef10 */
                    /* catch() { ... } // from try @ 00bbeab4 with catch @ 00bbef14 */
        puVar3 = (undefined8 *)FUN_00bd1f4c(param_1,&local_28,local_50);
        return puVar3;
      }
      return (undefined8 *)0x0;
    case 'O':
    case 'o':
    case 'w':
    case 'x':
      goto code_r0x00bbe964;
    case 'T':
    case 't':
      puVar3 = (undefined8 *)FUN_00bc2090(param_1);
      break;
    case 'a':
      puVar7 = &DAT_002925bc;
      goto LAB_00bbf0f0;
    case 'c':
      pcVar8 = "decltype(auto)";
      goto LAB_00bbf168;
    case 'd':
      pcVar8 = "decimal64";
      goto LAB_00bbf0bc;
    case 'e':
      *param_1 = (long)(pcVar12 + 2);
      puVar3 = (undefined8 *)FUN_00bd1ca8(param_1,"decimal128");
      return puVar3;
    case 'f':
      pcVar8 = "decimal32";
LAB_00bbf0bc:
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bbf028 with catch @ 00bbf0c0
                       try { // try from 00bbf0c0 to 00cbf0c3 has its CatchHandler @ 00bbefcc */
                    /* try { // try from 00bbf0c4 to 00cbf0c7 has its CatchHandler @ 00bbf0dc */
      *param_1 = (long)(pcVar12 + 2);
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bbf0c4 with catch @ 00bbf0dc
                        */
                    /* try { // try from 00bbf0e0 to 00cbf11f has its CatchHandler @ 00bbf0e0
                       catch() { ... } // from try @ 00bbf0e0 with catch @ 00bbf0e0
                       catch() { ... } // from try @ 00bbf390 with catch @ 00bbf0e0
                       catch() { ... } // from try @ 00bbf428 with catch @ 00bbf0e0 */
      puVar3 = (undefined8 *)FUN_00bd1b50(param_1,pcVar8);
      return puVar3;
    case 'h':
      puVar7 = &DAT_002a91e6;
LAB_00bbf0f0:
      *param_1 = (long)(pcVar12 + 2);
      puVar3 = (undefined8 *)FUN_00bc2bd8(param_1,puVar7);
      return puVar3;
    case 'i':
      pcVar8 = "char32_t";
      goto LAB_00bbf124;
    case 'n':
      pcVar8 = "std::nullptr_t";
LAB_00bbf168:
                    /* try { // try from 00bbf16c to 00cbf173 has its CatchHandler @ 00bbf518 */
      *param_1 = (long)(pcVar12 + 2);
      puVar3 = (undefined8 *)FUN_00bd0280(param_1,pcVar8);
      return puVar3;
    case 'p':
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bbf0c0 with catch @ 00bbefcc
                        */
      *param_1 = (long)(pcVar12 + 2);
      local_50._0_8_ = FUN_00bbde5c(param_1);
      if ((byte *)local_50._0_8_ == (byte *)0x0) {
        return (undefined8 *)0x0;
      }
      puVar3 = (undefined8 *)FUN_00bc6374(param_1,local_50);
      goto LAB_00bbe89c;
    case 's':
                    /* try { // try from 00bbf120 to 00cbf12b has its CatchHandler @ 00bbf530 */
      pcVar8 = "char16_t";
LAB_00bbf124:
      *param_1 = (long)(pcVar12 + 2);
      puVar3 = (undefined8 *)FUN_00bd1bfc(param_1,pcVar8);
      return puVar3;
    case 'u':
                    /* catch() { ... } // from try @ 00bbed78 with catch @ 00bbef80 */
                    /* catch() { ... } // from try @ 00bbe930 with catch @ 00bbef84 */
                    /* catch() { ... } // from try @ 00bbe8f8 with catch @ 00bbef88 */
      *param_1 = (long)(pcVar12 + 2);
      puVar3 = (undefined8 *)FUN_00bc9604(param_1,"char8_t");
      return puVar3;
    case 'v':
      puVar3 = (undefined8 *)FUN_00bd1ff8(param_1);
    }
    goto joined_r0x00bbef30;
  case 'F':
    goto code_r0x00bbe964;
  case 'G':
                    /* try { // try from 00bbe67c to 00cbe68b has its CatchHandler @ 00bbef30 */
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00bbde5c(param_1);
    if ((byte *)local_50._0_8_ == (byte *)0x0) {
      return (undefined8 *)0x0;
    }
    puVar3 = (undefined8 *)FUN_00bd261c(param_1,local_50);
    goto LAB_00bbe89c;
  case 'K':
  case 'V':
  case 'r':
    uVar15 = (ulong)(cVar1 == 'r');
                    /* try { // try from 00bbdec4 to 00cbdecf has its CatchHandler @ 00bbe19c */
    if (uVar15 < uVar5) {
      uVar14 = 1;
                    /* try { // try from 00bbded0 to 00cbdf0f has its CatchHandler @ 00bbe1a4 */
      if (cVar1 == 'r') {
        uVar14 = 2;
      }
      if (pcVar12[uVar15] != 'V') {
        uVar14 = (uint)(cVar1 == 'r');
      }
      uVar15 = (ulong)uVar14;
    }
    if (uVar15 < uVar5) {
      uVar14 = (uint)uVar15;
      if (pcVar12[uVar15] == 'K') {
        uVar14 = uVar14 + 1;
      }
      uVar15 = (ulong)uVar14;
    }
                    /* try { // try from 00bbdf28 to 00cbdf33 has its CatchHandler @ 00bbe198 */
                    /* try { // try from 00bbdf34 to 00cbe1cf has its CatchHandler @ 00bbd464 */
    if ((uVar5 <= uVar15) ||
       ((pcVar12[uVar15] != 'F' &&
        ((((pcVar12[uVar15] != 'D' || (uVar5 <= uVar15 + 1)) ||
          (0x29 < (byte)pcVar12[uVar15 + 1] - 0x4f)) ||
         ((1L << ((ulong)((byte)pcVar12[uVar15 + 1] - 0x4f) & 0x3f) & 0x30100000001U) == 0))))))
    goto code_r0x00bbdf5c;
    goto code_r0x00bbe964;
  case 'M':
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00bbde5c(param_1);
                    /* try { // try from 00bbe6b0 to 00cbe6bb has its CatchHandler @ 00bbef34 */
    puVar3 = (undefined8 *)0x0;
    if ((byte *)local_50._0_8_ != (byte *)0x0) {
                    /* try { // try from 00bbe6bc to 00cbe6cb has its CatchHandler @ 00bbef30 */
      local_28 = FUN_00bbde5c(param_1);
      puVar3 = (undefined8 *)0x0;
      if (local_28 != 0) {
        puVar3 = (undefined8 *)FUN_00bd4008(param_1,local_50,&local_28);
      }
    }
    goto joined_r0x00bbef30;
  case 'O':
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00bbde5c(param_1);
    if ((byte *)local_50._0_8_ == (byte *)0x0) {
      return (undefined8 *)0x0;
    }
    local_28 = CONCAT44(local_28._4_4_,1);
    goto LAB_00bbebac;
  case 'P':
                    /* try { // try from 00bbebc8 to 00cbebcb has its CatchHandler @ 00bbef40 */
                    /* try { // try from 00bbebcc to 00cbec1b has its CatchHandler @ 00bbe1d0 */
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00bbde5c(param_1);
    if ((byte *)local_50._0_8_ == (byte *)0x0) {
      return (undefined8 *)0x0;
    }
    puVar3 = (undefined8 *)FUN_00bd2404(param_1,local_50);
    goto LAB_00bbe89c;
  case 'R':
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00bbde5c(param_1);
    if ((byte *)local_50._0_8_ == (byte *)0x0) {
      return (undefined8 *)0x0;
    }
    local_28 = local_28 & 0xffffffff00000000;
LAB_00bbebac:
    puVar3 = (undefined8 *)FUN_00bd24b0(param_1,local_50,&local_28);
    goto LAB_00bbe89c;
  case 'S':
                    /* try { // try from 00bbe880 to 00cbe893 has its CatchHandler @ 00bbee50 */
    if ((uVar5 < 2) || (pcVar12[1] != 't')) {
      local_28 = (ulong)local_28._1_7_ << 8;
      puVar3 = (undefined8 *)FUN_00bc15e4(param_1,0,&local_28);
      if (puVar3 == (undefined8 *)0x0) {
        return (undefined8 *)0x0;
      }
                    /* try { // try from 00bbedac to 00cbedb3 has its CatchHandler @ 00bbef78 */
      local_58 = puVar3;
      if (((char *)param_1[1] == (char *)*param_1) || (*(char *)*param_1 != 'I')) {
                    /* catch() { ... } // from try @ 00bbe4a8 with catch @ 00bbeeb0 */
        if ((local_28 & 0xff) != 0) {
          return puVar3;
        }
        goto LAB_00bbe89c;
      }
                    /* try { // try from 00bbedc8 to 00cbedcf has its CatchHandler @ 00bbef50 */
      if (((char)local_28 != '\0') && ((char)param_1[0x61] == '\0')) {
        return puVar3;
      }
      if ((char)local_28 == '\0') {
        FUN_00bbfdf8(param_1 + 0x25,&local_58);
      }
                    /* try { // try from 00bbede4 to 00cbede7 has its CatchHandler @ 00bbef78 */
      local_50._0_8_ = FUN_00bc1754(param_1,0);
      if ((byte *)local_50._0_8_ == (byte *)0x0) {
        return (undefined8 *)0x0;
      }
LAB_00bbedf4:
                    /* try { // try from 00bbedfc to 00cbedff has its CatchHandler @ 00bbef50 */
      puVar3 = (undefined8 *)FUN_00bc1c24(param_1,&local_58,local_50);
      goto LAB_00bbe89c;
    }
    goto code_r0x00bbe890;
  case 'T':
    if (((uVar5 < 2) || (0x10 < (byte)pcVar12[1] - 0x65)) ||
       ((1 << (ulong)((byte)pcVar12[1] - 0x65 & 0x1f) & 0x14001U) == 0)) {
      puVar3 = (undefined8 *)FUN_00bc1ccc(param_1);
      if (puVar3 == (undefined8 *)0x0) {
        return (undefined8 *)0x0;
      }
      local_58 = puVar3;
      if ((((char)param_1[0x61] == '\0') || ((char *)param_1[1] == (char *)*param_1)) ||
         (*(char *)*param_1 != 'I')) goto LAB_00bbe89c;
      local_50._0_8_ = FUN_00bc1754(param_1,0);
                    /* try { // try from 00bbe2a0 to 00cbe2ab has its CatchHandler @ 00bbeee4 */
      if ((byte *)local_50._0_8_ == (byte *)0x0) {
        return (undefined8 *)0x0;
      }
      goto LAB_00bbedf4;
    }
code_r0x00bbe890:
    puVar3 = (undefined8 *)FUN_00bd22b4(param_1);
    goto joined_r0x00bbef30;
  case 'U':
code_r0x00bbdf5c:
    puVar3 = (undefined8 *)FUN_00bd1778(param_1);
joined_r0x00bbef30:
                    /* catch() { ... } // from try @ 00bbe67c with catch @ 00bbef30
                       catch() { ... } // from try @ 00bbe6bc with catch @ 00bbef30
                       catch() { ... } // from try @ 00bbe6fc with catch @ 00bbef30
                       catch() { ... } // from try @ 00bbe73c with catch @ 00bbef30
                       catch() { ... } // from try @ 00bbe77c with catch @ 00bbef30
                       catch() { ... } // from try @ 00bbe7bc with catch @ 00bbef30 */
    if (puVar3 == (undefined8 *)0x0) {
      return (undefined8 *)0x0;
    }
LAB_00bbe89c:
    plVar18 = (long *)param_1[0x26];
    if (plVar18 == (long *)param_1[0x27]) {
      __src = (long *)param_1[0x25];
                    /* try { // try from 00bbe8b0 to 00cbe8c7 has its CatchHandler @ 00bbef68 */
      __n = (long)plVar18 - (long)__src;
      if (__src == param_1 + 0x28) {
                    /* try { // try from 00bbe8d8 to 00cbe8df has its CatchHandler @ 00bbef4c */
        pvVar4 = malloc(__n * 2);
        if (pvVar4 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
          abort();
        }
        if (plVar18 != __src) {
                    /* try { // try from 00bbe8f8 to 00cbe927 has its CatchHandler @ 00bbef88 */
          memmove(pvVar4,__src,__n);
        }
        param_1[0x25] = (long)pvVar4;
      }
      else {
        pvVar4 = realloc(__src,__n * 2);
        param_1[0x25] = (long)pvVar4;
        if (pvVar4 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
          abort();
        }
      }
      plVar18 = (long *)((long)pvVar4 + __n);
      param_1[0x27] = (long)((long)pvVar4 + ((long)__n >> 2) * 8);
    }
    param_1[0x26] = (long)(plVar18 + 1);
    *plVar18 = (long)puVar3;
    return puVar3;
  case 'a':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) {
LAB_00bbf1ec:
                    /* WARNING: Subroutine does not return */
        _ZSt9terminatev();
      }
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "signed char";
    goto LAB_00bbecd8;
  case 'b':
                    /* try { // try from 00bbe2ac to 00cbe2bb has its CatchHandler @ 00bbeecc */
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
                    /* try { // try from 00bbe2bc to 00cbe2cf has its CatchHandler @ 00bbeeb4 */
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "bool";
    goto LAB_00bbed58;
  case 'c':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "char";
    goto LAB_00bbed58;
  case 'd':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
                    /* try { // try from 00bbe3ec to 00cbe3ef has its CatchHandler @ 00bbef3c */
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
                    /* try { // try from 00bbe3f0 to 00cbe467 has its CatchHandler @ 00bbe1d0 */
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "double";
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    uVar11 = 6;
    break;
  case 'e':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
                    /* try { // try from 00bbea50 to 00cbeab3 has its CatchHandler @ 00bbe1d0 */
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "long double";
LAB_00bbecd8:
    *(ushort *)((long)puVar2 + 9) = uVar9 & 0xf000 | 0x540;
    uVar11 = 0xb;
    break;
  case 'f':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
                    /* try { // try from 00bbe1d0 to 00cbe217 has its CatchHandler @ 00bbe1d0
                       catch() { ... } // from try @ 00bbe1d0 with catch @ 00bbe1d0
                       catch() { ... } // from try @ 00bbe3f0 with catch @ 00bbe1d0
                       catch() { ... } // from try @ 00bbe998 with catch @ 00bbe1d0
                       catch() { ... } // from try @ 00bbea50 with catch @ 00bbe1d0
                       catch() { ... } // from try @ 00bbeabc with catch @ 00bbe1d0
                       catch() { ... } // from try @ 00bbebcc with catch @ 00bbe1d0
                       catch() { ... } // from try @ 00bbee50 with catch @ 00bbe1d0 */
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
                    /* try { // try from 00bbe218 to 00cbe21f has its CatchHandler @ 00bbef08 */
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "float";
    goto LAB_00bbe74c;
  case 'g':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
                    /* try { // try from 00bbe468 to 00cbe46f has its CatchHandler @ 00bbef48 */
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "__float128";
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    uVar11 = 10;
    break;
  case 'h':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00bbe998 to 00cbe9df has its CatchHandler @ 00bbe1d0 */
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "unsigned char";
    goto LAB_00bbe9e0;
  case 'i':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
                    /* try { // try from 00bbe5d8 to 00cbe5e3 has its CatchHandler @ 00bbee80 */
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00bbe5e4 to 00cbe5f3 has its CatchHandler @ 00bbee6c */
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
                    /* try { // try from 00bbe5f4 to 00cbe607 has its CatchHandler @ 00bbee54 */
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "int";
    goto LAB_00bbe630;
  case 'j':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
                    /* try { // try from 00bbeab4 to 00cbeabb has its CatchHandler @ 00bbef14 */
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
                    /* try { // try from 00bbeabc to 00cbeae3 has its CatchHandler @ 00bbe1d0 */
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
                    /* try { // try from 00bbeae4 to 00cbeaef has its CatchHandler @ 00bbef4c */
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "unsigned int";
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    uVar11 = 0xc;
    break;
  case 'l':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "long";
    goto LAB_00bbed58;
  case 'm':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
                    /* catch() { ... } // from try @ 00bbd4e8 with catch @ 00bbe178 */
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
                    /* catch() { ... } // from try @ 00bbd554 with catch @ 00bbe188
                       catch() { ... } // from try @ 00bbd5c8 with catch @ 00bbe188
                       catch() { ... } // from try @ 00bbd63c with catch @ 00bbe188 */
                    /* catch() { ... } // from try @ 00bbdcc4 with catch @ 00bbe18c
                       catch() { ... } // from try @ 00bbdd04 with catch @ 00bbe18c
                       catch() { ... } // from try @ 00bbdd44 with catch @ 00bbe18c
                       catch() { ... } // from try @ 00bbdd84 with catch @ 00bbe18c */
                    /* catch() { ... } // from try @ 00bbdcb8 with catch @ 00bbe190
                       catch() { ... } // from try @ 00bbdcf8 with catch @ 00bbe190
                       catch() { ... } // from try @ 00bbdd38 with catch @ 00bbe190
                       catch() { ... } // from try @ 00bbdd78 with catch @ 00bbe190 */
                    /* catch() { ... } // from try @ 00bbd560 with catch @ 00bbe194
                       catch() { ... } // from try @ 00bbd5d4 with catch @ 00bbe194
                       catch() { ... } // from try @ 00bbd648 with catch @ 00bbe194 */
                    /* catch() { ... } // from try @ 00bbd6b0 with catch @ 00bbe198
                       catch() { ... } // from try @ 00bbd838 with catch @ 00bbe198
                       catch() { ... } // from try @ 00bbd984 with catch @ 00bbe198
                       catch() { ... } // from try @ 00bbdad0 with catch @ 00bbe198
                       catch() { ... } // from try @ 00bbdba4 with catch @ 00bbe198
                       catch() { ... } // from try @ 00bbdbe4 with catch @ 00bbe198
                       catch() { ... } // from try @ 00bbddb8 with catch @ 00bbe198
                       catch() { ... } // from try @ 00bbdf28 with catch @ 00bbe198 */
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
                    /* catch() { ... } // from try @ 00bbdec4 with catch @ 00bbe19c */
                    /* catch() { ... } // from try @ 00bbd7d4 with catch @ 00bbe1a0 */
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
                    /* catch() { ... } // from try @ 00bbded0 with catch @ 00bbe1a4 */
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
                    /* catch() { ... } // from try @ 00bbd7e0 with catch @ 00bbe1a8 */
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "unsigned long";
LAB_00bbe9e0:
                    /* try { // try from 00bbe9e0 to 00cbea4f has its CatchHandler @ 00bbef44 */
    *(ushort *)((long)puVar2 + 9) = uVar9 & 0xf000 | 0x540;
    uVar11 = 0xd;
    break;
  case 'n':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
                    /* catch() { ... } // from try @ 00bbd884 with catch @ 00bbe0e0 */
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
                    /* catch() { ... } // from try @ 00bbd878 with catch @ 00bbe0f4 */
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
                    /* catch() { ... } // from try @ 00bbd70c with catch @ 00bbe0f8 */
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
                    /* catch() { ... } // from try @ 00bbd6fc with catch @ 00bbe110 */
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
                    /* catch() { ... } // from try @ 00bbd6f0 with catch @ 00bbe124 */
                    /* catch() { ... } // from try @ 00bbd504 with catch @ 00bbe128 */
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
                    /* catch() { ... } // from try @ 00bbd4f4 with catch @ 00bbe140 */
    *(char **)((long)puVar3 + lVar10 + 0x20) = "__int128";
    *(undefined8 *)((long)puVar3 + lVar10 + 0x28) = 8;
    return puVar2;
  case 'o':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00bbe568 to 00cbe573 has its CatchHandler @ 00bbef6c */
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
                    /* try { // try from 00bbe574 to 00cbe583 has its CatchHandler @ 00bbef70 */
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
                    /* try { // try from 00bbe598 to 00cbe59f has its CatchHandler @ 00bbef48 */
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "unsigned __int128";
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    uVar11 = 0x11;
    break;
  case 's':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
                    /* try { // try from 00bbe6f0 to 00cbe6fb has its CatchHandler @ 00bbef34 */
    lVar10 = *(long *)((long)pvVar4 + 8);
                    /* try { // try from 00bbe6fc to 00cbe70b has its CatchHandler @ 00bbef30 */
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
                    /* try { // try from 00bbe730 to 00cbe73b has its CatchHandler @ 00bbef34 */
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
                    /* try { // try from 00bbe73c to 00cbe74b has its CatchHandler @ 00bbef30 */
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "short";
LAB_00bbe74c:
    *(ushort *)((long)puVar2 + 9) = uVar9 & 0xf000 | 0x540;
    uVar11 = 5;
    break;
  case 't':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "unsigned short";
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    uVar11 = 0xe;
    break;
  case 'u':
    pbVar13 = (byte *)(pcVar12 + 1);
    *param_1 = (long)pbVar13;
                    /* try { // try from 00bbe770 to 00cbe77b has its CatchHandler @ 00bbef34 */
    if (pbVar6 == pbVar13) {
      return (undefined8 *)0x0;
    }
                    /* try { // try from 00bbe77c to 00cbe78b has its CatchHandler @ 00bbef30 */
    if (*pbVar13 - 0x3a < 0xfffffff6) {
      return (undefined8 *)0x0;
    }
    local_50._8_8_ = 0;
    lVar10 = 0;
    do {
      lVar17 = lVar10;
      uVar16 = local_50._8_8_;
      local_50._0_8_ = pcVar12 + lVar17 + 2;
      *param_1 = local_50._0_8_;
      uVar15 = (ulong)(byte)pcVar12[lVar17 + 1];
                    /* try { // try from 00bbe7b0 to 00cbe7bb has its CatchHandler @ 00bbef34 */
      local_50._8_8_ = (uVar15 + uVar16 * 10) - 0x30;
      if ((byte *)local_50._0_8_ == pbVar6) break;
                    /* try { // try from 00bbe7bc to 00cbe7cb has its CatchHandler @ 00bbef30 */
      lVar10 = lVar17 + 1;
    } while (*(byte *)local_50._0_8_ - 0x30 < 10);
    if ((uVar5 - lVar17) - 2 < (ulong)local_50._8_8_) {
      return (undefined8 *)0x0;
    }
                    /* try { // try from 00bbe7f0 to 00cbe81f has its CatchHandler @ 00bbef48 */
    pbVar13 = (byte *)(pcVar12 + uVar15 + uVar16 * 10 + lVar17 + -0x2e);
    *param_1 = (long)pbVar13;
    if (local_50._8_8_ == 0) {
      return (undefined8 *)0x0;
    }
    if ((pbVar13 == pbVar6) || (*pbVar13 != 0x49)) {
      puVar3 = (undefined8 *)FUN_00bc136c(param_1,local_50);
    }
    else {
      *param_1 = (long)(pcVar12 + uVar15 + uVar16 * 10 + lVar17 + -0x2d);
      local_28 = FUN_00bbde5c(param_1);
      if (local_28 == 0) {
        return (undefined8 *)0x0;
      }
      pcVar12 = (char *)*param_1;
      if (pcVar12 == (char *)param_1[1]) {
        return (undefined8 *)0x0;
      }
      if (*pcVar12 != 'E') {
        return (undefined8 *)0x0;
      }
      *param_1 = (long)(pcVar12 + 1);
      puVar3 = (undefined8 *)FUN_00bd1d54(param_1,local_50,&local_28);
    }
    goto LAB_00bbe89c;
  case 'v':
                    /* catch() { ... } // from try @ 00bbdbb0 with catch @ 00bbdff0 */
                    /* catch() { ... } // from try @ 00bbda5c with catch @ 00bbdff4 */
    pvVar4 = (void *)param_1[0x266];
                    /* catch() { ... } // from try @ 00bbd910 with catch @ 00bbdff8 */
    *param_1 = (long)(pcVar12 + 1);
                    /* catch() { ... } // from try @ 00bbde20 with catch @ 00bbdffc */
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
                    /* catch() { ... } // from try @ 00bbde10 with catch @ 00bbe014 */
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
                    /* catch() { ... } // from try @ 00bbde04 with catch @ 00bbe028 */
                    /* catch() { ... } // from try @ 00bbddc0 with catch @ 00bbe02c */
                    /* catch() { ... } // from try @ 00bbdc3c with catch @ 00bbe030 */
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
                    /* catch() { ... } // from try @ 00bbdc2c with catch @ 00bbe048 */
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "void";
LAB_00bbed58:
    *(ushort *)((long)puVar2 + 9) = uVar9 & 0xf000 | 0x540;
    uVar11 = 4;
    break;
  case 'w':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
                    /* try { // try from 00bbe368 to 00cbe373 has its CatchHandler @ 00bbef74 */
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
                    /* try { // try from 00bbe378 to 00cbe387 has its CatchHandler @ 00bbef64 */
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "wchar_t";
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    uVar11 = 7;
    break;
  case 'x':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
                    /* try { // try from 00bbec1c to 00cbec2f has its CatchHandler @ 00bbef48 */
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "long long";
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    uVar11 = 9;
    break;
  case 'y':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "unsigned long long";
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    uVar11 = 0x12;
    break;
  case 'z':
                    /* catch() { ... } // from try @ 00bbdb28 with catch @ 00bbe060 */
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
                    /* catch() { ... } // from try @ 00bbdb18 with catch @ 00bbe078 */
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00bbf1ec;
      lVar10 = 0;
                    /* catch() { ... } // from try @ 00bbdb0c with catch @ 00bbe08c */
      *puVar3 = pvVar4;
      puVar3[1] = 0;
                    /* catch() { ... } // from try @ 00bbda68 with catch @ 00bbe090 */
                    /* catch() { ... } // from try @ 00bbd9e0 with catch @ 00bbe094 */
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
                    /* catch() { ... } // from try @ 00bbd9d0 with catch @ 00bbe0ac */
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c17898;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
                    /* catch() { ... } // from try @ 00bbd9c4 with catch @ 00bbe0c0 */
                    /* catch() { ... } // from try @ 00bbd91c with catch @ 00bbe0c4 */
    pcVar12 = "...";
                    /* catch() { ... } // from try @ 00bbd894 with catch @ 00bbe0c8 */
LAB_00bbe630:
    *(ushort *)((long)puVar2 + 9) = uVar9 & 0xf000 | 0x540;
    uVar11 = 3;
  }
  puVar2[2] = pcVar12;
  puVar2[3] = uVar11;
code_r0x00bbed70:
                    /* try { // try from 00bbed78 to 00cbed97 has its CatchHandler @ 00bbef80 */
  return puVar2;
code_r0x00bbe964:
  puVar3 = (undefined8 *)FUN_00bd11d0(param_1);
  goto joined_r0x00bbef30;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbde5c"></a> `00bbde5c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbde60"></a> `00bbde60` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbde64"></a> `00bbde64` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbde68"></a> `00bbde68` | `f7 1b 00 f9` | str x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbde6c"></a> `00bbde6c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbde70"></a> `00bbde70` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbde74"></a> `00bbde74` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bbde78"></a> `00bbde78` | `08 28 40 a9` | ldp x8,x10,[x0] | `FALL_THROUGH`
<a id="insn-00bbde7c"></a> `00bbde7c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbde80"></a> `00bbde80` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbde84"></a> `00bbde84` | `49 01 08 eb` | subs x9,x10,x8 | `FALL_THROUGH`
<a id="insn-00bbde88"></a> `00bbde88` | `20 50 00 54` | b.eq 0x00bbe88c | `CONDITIONAL_JUMP`
<a id="insn-00bbde8c"></a> `00bbde8c` | `0b 01 40 39` | ldrb w11,[x8] | `FALL_THROUGH`
<a id="insn-00bbde90"></a> `00bbde90` | `6c 05 01 51` | sub w12,w11,#0x41 | `FALL_THROUGH`
<a id="insn-00bbde94"></a> `00bbde94` | `9f e5 00 71` | cmp w12,#0x39 | `FALL_THROUGH`
<a id="insn-00bbde98"></a> `00bbde98` | `a8 4f 00 54` | b.hi 0x00bbe88c | `CONDITIONAL_JUMP`
<a id="insn-00bbde9c"></a> `00bbde9c` | `ed b9 ff f0` | adrp x13,0x2fc000 | `FALL_THROUGH`
<a id="insn-00bbdea0"></a> `00bbdea0` | `ad a1 2d 91` | add x13,x13,#0xb68 | `FALL_THROUGH`
<a id="insn-00bbdea4"></a> `00bbdea4` | `8e 00 00 10` | adr x14,0xbbdeb4 | `FALL_THROUGH`
<a id="insn-00bbdea8"></a> `00bbdea8` | `af 79 6c 78` | ldrh w15,[x13, x12, LSL #0x1] | `FALL_THROUGH`
<a id="insn-00bbdeac"></a> `00bbdeac` | `ce 09 0f 8b` | add x14,x14,x15, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bbdeb0"></a> `00bbdeb0` | `c0 01 1f d6` | br x14 | `COMPUTED_JUMP`
<a id="insn-00bbdeb4"></a> `00bbdeb4` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbdeb8"></a> `00bbdeb8` | `7f c9 01 71` | cmp w11,#0x72 | `FALL_THROUGH`
<a id="insn-00bbdebc"></a> `00bbdebc` | `ea 17 9f 1a` | cset w10,eq | `FALL_THROUGH`
<a id="insn-00bbdec0"></a> `00bbdec0` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbdec4"></a> `00bbdec4` | `09 01 00 54` | b.ls 0x00bbdee4 | `CONDITIONAL_JUMP`
<a id="insn-00bbdec8"></a> `00bbdec8` | `0c 69 6a 38` | ldrb w12,[x8, x10, LSL ] | `FALL_THROUGH`
<a id="insn-00bbdecc"></a> `00bbdecc` | `7f c9 01 71` | cmp w11,#0x72 | `FALL_THROUGH`
<a id="insn-00bbded0"></a> `00bbded0` | `2b 00 80 52` | mov w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbded4"></a> `00bbded4` | `6b 15 8b 1a` | cinc w11,w11,eq | `FALL_THROUGH`
<a id="insn-00bbded8"></a> `00bbded8` | `8c 1d 00 12` | and w12,w12,#0xff | `FALL_THROUGH`
<a id="insn-00bbdedc"></a> `00bbdedc` | `9f 59 01 71` | cmp w12,#0x56 | `FALL_THROUGH`
<a id="insn-00bbdee0"></a> `00bbdee0` | `6a 01 8a 1a` | csel w10,w11,w10,eq | `FALL_THROUGH`
<a id="insn-00bbdee4"></a> `00bbdee4` | `eb 03 0a 2a` | mov w11,w10 | `FALL_THROUGH`
<a id="insn-00bbdee8"></a> `00bbdee8` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-00bbdeec"></a> `00bbdeec` | `c9 00 00 54` | b.ls 0x00bbdf04 | `CONDITIONAL_JUMP`
<a id="insn-00bbdef0"></a> `00bbdef0` | `0b 69 6b 38` | ldrb w11,[x8, x11, LSL ] | `FALL_THROUGH`
<a id="insn-00bbdef4"></a> `00bbdef4` | `6b 1d 00 12` | and w11,w11,#0xff | `FALL_THROUGH`
<a id="insn-00bbdef8"></a> `00bbdef8` | `7f 2d 01 71` | cmp w11,#0x4b | `FALL_THROUGH`
<a id="insn-00bbdefc"></a> `00bbdefc` | `4b 15 8a 1a` | cinc w11,w10,eq | `FALL_THROUGH`
<a id="insn-00bbdf00"></a> `00bbdf00` | `ea 03 0b 2a` | mov w10,w11 | `FALL_THROUGH`
<a id="insn-00bbdf04"></a> `00bbdf04` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-00bbdf08"></a> `00bbdf08` | `89 02 00 54` | b.ls 0x00bbdf58 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf0c"></a> `00bbdf0c` | `0b 69 6b 38` | ldrb w11,[x8, x11, LSL ] | `FALL_THROUGH`
<a id="insn-00bbdf10"></a> `00bbdf10` | `7f 19 01 71` | cmp w11,#0x46 | `FALL_THROUGH`
<a id="insn-00bbdf14"></a> `00bbdf14` | `60 52 00 54` | b.eq 0x00bbe960 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf18"></a> `00bbdf18` | `7f 11 01 71` | cmp w11,#0x44 | `FALL_THROUGH`
<a id="insn-00bbdf1c"></a> `00bbdf1c` | `e1 01 00 54` | b.ne 0x00bbdf58 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf20"></a> `00bbdf20` | `ea 03 0a 2a` | mov w10,w10 | `FALL_THROUGH`
<a id="insn-00bbdf24"></a> `00bbdf24` | `4a 05 00 91` | add x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdf28"></a> `00bbdf28` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbdf2c"></a> `00bbdf2c` | `69 01 00 54` | b.ls 0x00bbdf58 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf30"></a> `00bbdf30` | `08 69 6a 38` | ldrb w8,[x8, x10, LSL ] | `FALL_THROUGH`
<a id="insn-00bbdf34"></a> `00bbdf34` | `08 3d 01 51` | sub w8,w8,#0x4f | `FALL_THROUGH`
<a id="insn-00bbdf38"></a> `00bbdf38` | `1f a5 00 71` | cmp w8,#0x29 | `FALL_THROUGH`
<a id="insn-00bbdf3c"></a> `00bbdf3c` | `e8 00 00 54` | b.hi 0x00bbdf58 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf40"></a> `00bbdf40` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdf44"></a> `00bbdf44` | `28 21 c8 9a` | lsl x8,x9,x8 | `FALL_THROUGH`
<a id="insn-00bbdf48"></a> `00bbdf48` | `29 00 80 d2` | mov x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdf4c"></a> `00bbdf4c` | `29 60 c0 f2` | movk x9,#0x301, LSL #32 | `FALL_THROUGH`
<a id="insn-00bbdf50"></a> `00bbdf50` | `1f 01 09 ea` | tst x8,x9 | `FALL_THROUGH`
<a id="insn-00bbdf54"></a> `00bbdf54` | `61 50 00 54` | b.ne 0x00bbe960 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf58"></a> `00bbdf58` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbdf5c"></a> `00bbdf5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbdf60"></a> `00bbdf60` | `06 4e 00 94` | bl 0x00bd1778 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf64"></a> `00bbdf64` | `c0 49 00 b5` | cbnz x0,0x00bbe89c | `CONDITIONAL_JUMP`
<a id="insn-00bbdf68"></a> `00bbdf68` | `81 03 00 14` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdf6c"></a> `00bbdf6c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbdf70"></a> `00bbdf70` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdf74"></a> `00bbdf74` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbdf78"></a> `00bbdf78` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbdf7c"></a> `00bbdf7c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbdf80"></a> `00bbdf80` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbdf84"></a> `00bbdf84` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbdf88"></a> `00bbdf88` | `08 01 00 54` | b.hi 0x00bbdfa8 | `CONDITIONAL_JUMP`
<a id="insn-00bbdf8c"></a> `00bbdf8c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbdf90"></a> `00bbdf90` | `90 7c 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbdf94"></a> `00bbdf94` | `c0 92 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbdf98"></a> `00bbdf98` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbdf9c"></a> `00bbdf9c` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbdfa0"></a> `00bbdfa0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbdfa4"></a> `00bbdfa4` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbdfa8"></a> `00bbdfa8` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbdfac"></a> `00bbdfac` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbdfb0"></a> `00bbdfb0` | `c8 02 00 d0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbdfb4"></a> `00bbdfb4` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbdfb8"></a> `00bbdfb8` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbdfbc"></a> `00bbdfbc` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbdfc0"></a> `00bbdfc0` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbdfc4"></a> `00bbdfc4` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbdfc8"></a> `00bbdfc8` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbdfcc"></a> `00bbdfcc` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbdfd0"></a> `00bbdfd0` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbdfd4"></a> `00bbdfd4` | `89 b6 ff f0` | adrp x9,0x290000 | `FALL_THROUGH`
<a id="insn-00bbdfd8"></a> `00bbdfd8` | `29 1d 22 91` | add x9,x9,#0x887 | `FALL_THROUGH`
<a id="insn-00bbdfdc"></a> `00bbdfdc` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbdfe0"></a> `00bbdfe0` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbdfe4"></a> `00bbdfe4` | `48 02 80 52` | mov w8,#0x12 | `FALL_THROUGH`
<a id="insn-00bbdfe8"></a> `00bbdfe8` | `60 03 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbdfec"></a> `00bbdfec` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbdff0"></a> `00bbdff0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbdff4"></a> `00bbdff4` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbdff8"></a> `00bbdff8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbdffc"></a> `00bbdffc` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe000"></a> `00bbe000` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe004"></a> `00bbe004` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe008"></a> `00bbe008` | `08 01 00 54` | b.hi 0x00bbe028 | `CONDITIONAL_JUMP`
<a id="insn-00bbe00c"></a> `00bbe00c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe010"></a> `00bbe010` | `70 7c 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe014"></a> `00bbe014` | `c0 8e 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe018"></a> `00bbe018` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe01c"></a> `00bbe01c` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe020"></a> `00bbe020` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe024"></a> `00bbe024` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe028"></a> `00bbe028` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe02c"></a> `00bbe02c` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe030"></a> `00bbe030` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe034"></a> `00bbe034` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe038"></a> `00bbe038` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe03c"></a> `00bbe03c` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe040"></a> `00bbe040` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe044"></a> `00bbe044` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe048"></a> `00bbe048` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe04c"></a> `00bbe04c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe050"></a> `00bbe050` | `69 b7 ff f0` | adrp x9,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bbe054"></a> `00bbe054` | `29 9d 1e 91` | add x9,x9,#0x7a7 | `FALL_THROUGH`
<a id="insn-00bbe058"></a> `00bbe058` | `40 03 00 14` | b 0x00bbed58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe05c"></a> `00bbe05c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe060"></a> `00bbe060` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe064"></a> `00bbe064` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe068"></a> `00bbe068` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe06c"></a> `00bbe06c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe070"></a> `00bbe070` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe074"></a> `00bbe074` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe078"></a> `00bbe078` | `08 01 00 54` | b.hi 0x00bbe098 | `CONDITIONAL_JUMP`
<a id="insn-00bbe07c"></a> `00bbe07c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe080"></a> `00bbe080` | `54 7c 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe084"></a> `00bbe084` | `40 8b 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe088"></a> `00bbe088` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe08c"></a> `00bbe08c` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe090"></a> `00bbe090` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe094"></a> `00bbe094` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe098"></a> `00bbe098` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe09c"></a> `00bbe09c` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe0a0"></a> `00bbe0a0` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe0a4"></a> `00bbe0a4` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe0a8"></a> `00bbe0a8` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe0ac"></a> `00bbe0ac` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe0b0"></a> `00bbe0b0` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe0b4"></a> `00bbe0b4` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe0b8"></a> `00bbe0b8` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe0bc"></a> `00bbe0bc` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe0c0"></a> `00bbe0c0` | `e9 b6 ff 90` | adrp x9,0x29a000 | `FALL_THROUGH`
<a id="insn-00bbe0c4"></a> `00bbe0c4` | `29 ed 2b 91` | add x9,x9,#0xafb | `FALL_THROUGH`
<a id="insn-00bbe0c8"></a> `00bbe0c8` | `5a 01 00 14` | b 0x00bbe630 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe0cc"></a> `00bbe0cc` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe0d0"></a> `00bbe0d0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe0d4"></a> `00bbe0d4` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe0d8"></a> `00bbe0d8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe0dc"></a> `00bbe0dc` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe0e0"></a> `00bbe0e0` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe0e4"></a> `00bbe0e4` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe0e8"></a> `00bbe0e8` | `08 01 00 54` | b.hi 0x00bbe108 | `CONDITIONAL_JUMP`
<a id="insn-00bbe0ec"></a> `00bbe0ec` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe0f0"></a> `00bbe0f0` | `38 7c 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe0f4"></a> `00bbe0f4` | `c0 87 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe0f8"></a> `00bbe0f8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe0fc"></a> `00bbe0fc` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe100"></a> `00bbe100` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe104"></a> `00bbe104` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe108"></a> `00bbe108` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe10c"></a> `00bbe10c` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe110"></a> `00bbe110` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe114"></a> `00bbe114` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe118"></a> `00bbe118` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe11c"></a> `00bbe11c` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe120"></a> `00bbe120` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe124"></a> `00bbe124` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe128"></a> `00bbe128` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe12c"></a> `00bbe12c` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbe130"></a> `00bbe130` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe134"></a> `00bbe134` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbe138"></a> `00bbe138` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe13c"></a> `00bbe13c` | `a8 b6 ff b0` | adrp x8,0x293000 | `FALL_THROUGH`
<a id="insn-00bbe140"></a> `00bbe140` | `08 79 19 91` | add x8,x8,#0x65e | `FALL_THROUGH`
<a id="insn-00bbe144"></a> `00bbe144` | `08 24 01 a9` | stp x8,x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe148"></a> `00bbe148` | `09 03 00 14` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe14c"></a> `00bbe14c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe150"></a> `00bbe150` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe154"></a> `00bbe154` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe158"></a> `00bbe158` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe15c"></a> `00bbe15c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe160"></a> `00bbe160` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe164"></a> `00bbe164` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe168"></a> `00bbe168` | `08 01 00 54` | b.hi 0x00bbe188 | `CONDITIONAL_JUMP`
<a id="insn-00bbe16c"></a> `00bbe16c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe170"></a> `00bbe170` | `18 7c 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe174"></a> `00bbe174` | `c0 83 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe178"></a> `00bbe178` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe17c"></a> `00bbe17c` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe180"></a> `00bbe180` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe184"></a> `00bbe184` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe188"></a> `00bbe188` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe18c"></a> `00bbe18c` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe190"></a> `00bbe190` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe194"></a> `00bbe194` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe198"></a> `00bbe198` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe19c"></a> `00bbe19c` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe1a0"></a> `00bbe1a0` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe1a4"></a> `00bbe1a4` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe1a8"></a> `00bbe1a8` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe1ac"></a> `00bbe1ac` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe1b0"></a> `00bbe1b0` | `69 b7 ff f0` | adrp x9,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bbe1b4"></a> `00bbe1b4` | `29 b1 1e 91` | add x9,x9,#0x7ac | `FALL_THROUGH`
<a id="insn-00bbe1b8"></a> `00bbe1b8` | `0a 02 00 14` | b 0x00bbe9e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe1bc"></a> `00bbe1bc` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe1c0"></a> `00bbe1c0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe1c4"></a> `00bbe1c4` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe1c8"></a> `00bbe1c8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe1cc"></a> `00bbe1cc` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe1d0"></a> `00bbe1d0` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe1d4"></a> `00bbe1d4` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe1d8"></a> `00bbe1d8` | `08 01 00 54` | b.hi 0x00bbe1f8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe1dc"></a> `00bbe1dc` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe1e0"></a> `00bbe1e0` | `fc 7b 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe1e4"></a> `00bbe1e4` | `40 80 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe1e8"></a> `00bbe1e8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe1ec"></a> `00bbe1ec` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe1f0"></a> `00bbe1f0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe1f4"></a> `00bbe1f4` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe1f8"></a> `00bbe1f8` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe1fc"></a> `00bbe1fc` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe200"></a> `00bbe200` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe204"></a> `00bbe204` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe208"></a> `00bbe208` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe20c"></a> `00bbe20c` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe210"></a> `00bbe210` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe214"></a> `00bbe214` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe218"></a> `00bbe218` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe21c"></a> `00bbe21c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe220"></a> `00bbe220` | `69 b7 ff b0` | adrp x9,0x2ab000 | `FALL_THROUGH`
<a id="insn-00bbe224"></a> `00bbe224` | `29 ad 01 91` | add x9,x9,#0x6b | `FALL_THROUGH`
<a id="insn-00bbe228"></a> `00bbe228` | `49 01 00 14` | b 0x00bbe74c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe22c"></a> `00bbe22c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe230"></a> `00bbe230` | `3f 09 00 f1` | cmp x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bbe234"></a> `00bbe234` | `63 01 00 54` | b.cc 0x00bbe260 | `CONDITIONAL_JUMP`
<a id="insn-00bbe238"></a> `00bbe238` | `08 05 40 39` | ldrb w8,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bbe23c"></a> `00bbe23c` | `08 95 01 51` | sub w8,w8,#0x65 | `FALL_THROUGH`
<a id="insn-00bbe240"></a> `00bbe240` | `1f 41 00 71` | cmp w8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbe244"></a> `00bbe244` | `e8 00 00 54` | b.hi 0x00bbe260 | `CONDITIONAL_JUMP`
<a id="insn-00bbe248"></a> `00bbe248` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe24c"></a> `00bbe24c` | `28 21 c8 1a` | lsl w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00bbe250"></a> `00bbe250` | `29 00 88 52` | mov w9,#0x4001 | `FALL_THROUGH`
<a id="insn-00bbe254"></a> `00bbe254` | `29 00 a0 72` | movk w9,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-00bbe258"></a> `00bbe258` | `1f 01 09 6a` | tst w8,w9 | `FALL_THROUGH`
<a id="insn-00bbe25c"></a> `00bbe25c` | `81 31 00 54` | b.ne 0x00bbe88c | `CONDITIONAL_JUMP`
<a id="insn-00bbe260"></a> `00bbe260` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe264"></a> `00bbe264` | `9a 0e 00 94` | bl 0x00bc1ccc | `UNCONDITIONAL_CALL`
<a id="insn-00bbe268"></a> `00bbe268` | `e0 07 00 f9` | str x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe26c"></a> `00bbe26c` | `00 58 00 b4` | cbz x0,0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbe270"></a> `00bbe270` | `68 22 4c 39` | ldrb w8,[x19, #0x308] | `FALL_THROUGH`
<a id="insn-00bbe274"></a> `00bbe274` | `48 31 00 34` | cbz w8,0x00bbe89c | `CONDITIONAL_JUMP`
<a id="insn-00bbe278"></a> `00bbe278` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbe27c"></a> `00bbe27c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbe280"></a> `00bbe280` | `e0 30 00 54` | b.eq 0x00bbe89c | `CONDITIONAL_JUMP`
<a id="insn-00bbe284"></a> `00bbe284` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bbe288"></a> `00bbe288` | `1f 25 01 71` | cmp w8,#0x49 | `FALL_THROUGH`
<a id="insn-00bbe28c"></a> `00bbe28c` | `81 30 00 54` | b.ne 0x00bbe89c | `CONDITIONAL_JUMP`
<a id="insn-00bbe290"></a> `00bbe290` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe294"></a> `00bbe294` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbe298"></a> `00bbe298` | `2f 0d 00 94` | bl 0x00bc1754 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe29c"></a> `00bbe29c` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe2a0"></a> `00bbe2a0` | `a0 5a 00 b5` | cbnz x0,0x00bbedf4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe2a4"></a> `00bbe2a4` | `b2 02 00 14` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe2a8"></a> `00bbe2a8` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe2ac"></a> `00bbe2ac` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe2b0"></a> `00bbe2b0` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe2b4"></a> `00bbe2b4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe2b8"></a> `00bbe2b8` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe2bc"></a> `00bbe2bc` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe2c0"></a> `00bbe2c0` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe2c4"></a> `00bbe2c4` | `08 01 00 54` | b.hi 0x00bbe2e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe2c8"></a> `00bbe2c8` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe2cc"></a> `00bbe2cc` | `c1 7b 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe2d0"></a> `00bbe2d0` | `e0 78 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe2d4"></a> `00bbe2d4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe2d8"></a> `00bbe2d8` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe2dc"></a> `00bbe2dc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe2e0"></a> `00bbe2e0` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe2e4"></a> `00bbe2e4` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe2e8"></a> `00bbe2e8` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe2ec"></a> `00bbe2ec` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe2f0"></a> `00bbe2f0` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe2f4"></a> `00bbe2f4` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe2f8"></a> `00bbe2f8` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe2fc"></a> `00bbe2fc` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe300"></a> `00bbe300` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe304"></a> `00bbe304` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe308"></a> `00bbe308` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe30c"></a> `00bbe30c` | `c9 b6 ff 90` | adrp x9,0x296000 | `FALL_THROUGH`
<a id="insn-00bbe310"></a> `00bbe310` | `29 81 13 91` | add x9,x9,#0x4e0 | `FALL_THROUGH`
<a id="insn-00bbe314"></a> `00bbe314` | `91 02 00 14` | b 0x00bbed58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe318"></a> `00bbe318` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe31c"></a> `00bbe31c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe320"></a> `00bbe320` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe324"></a> `00bbe324` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe328"></a> `00bbe328` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe32c"></a> `00bbe32c` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe330"></a> `00bbe330` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe334"></a> `00bbe334` | `08 01 00 54` | b.hi 0x00bbe354 | `CONDITIONAL_JUMP`
<a id="insn-00bbe338"></a> `00bbe338` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe33c"></a> `00bbe33c` | `a5 7b 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe340"></a> `00bbe340` | `60 75 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe344"></a> `00bbe344` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe348"></a> `00bbe348` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe34c"></a> `00bbe34c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe350"></a> `00bbe350` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe354"></a> `00bbe354` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe358"></a> `00bbe358` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe35c"></a> `00bbe35c` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe360"></a> `00bbe360` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe364"></a> `00bbe364` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe368"></a> `00bbe368` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe36c"></a> `00bbe36c` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe370"></a> `00bbe370` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe374"></a> `00bbe374` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe378"></a> `00bbe378` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbe37c"></a> `00bbe37c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe380"></a> `00bbe380` | `89 b6 ff d0` | adrp x9,0x290000 | `FALL_THROUGH`
<a id="insn-00bbe384"></a> `00bbe384` | `29 c1 21 91` | add x9,x9,#0x870 | `FALL_THROUGH`
<a id="insn-00bbe388"></a> `00bbe388` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbe38c"></a> `00bbe38c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe390"></a> `00bbe390` | `e8 00 80 52` | mov w8,#0x7 | `FALL_THROUGH`
<a id="insn-00bbe394"></a> `00bbe394` | `75 02 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe398"></a> `00bbe398` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe39c"></a> `00bbe39c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe3a0"></a> `00bbe3a0` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe3a4"></a> `00bbe3a4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe3a8"></a> `00bbe3a8` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe3ac"></a> `00bbe3ac` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe3b0"></a> `00bbe3b0` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe3b4"></a> `00bbe3b4` | `08 01 00 54` | b.hi 0x00bbe3d4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe3b8"></a> `00bbe3b8` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe3bc"></a> `00bbe3bc` | `85 7b 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe3c0"></a> `00bbe3c0` | `60 71 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe3c4"></a> `00bbe3c4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe3c8"></a> `00bbe3c8` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe3cc"></a> `00bbe3cc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe3d0"></a> `00bbe3d0` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe3d4"></a> `00bbe3d4` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe3d8"></a> `00bbe3d8` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe3dc"></a> `00bbe3dc` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe3e0"></a> `00bbe3e0` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe3e4"></a> `00bbe3e4` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe3e8"></a> `00bbe3e8` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe3ec"></a> `00bbe3ec` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe3f0"></a> `00bbe3f0` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe3f4"></a> `00bbe3f4` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe3f8"></a> `00bbe3f8` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbe3fc"></a> `00bbe3fc` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe400"></a> `00bbe400` | `e9 b6 ff f0` | adrp x9,0x29d000 | `FALL_THROUGH`
<a id="insn-00bbe404"></a> `00bbe404` | `29 65 3c 91` | add x9,x9,#0xf19 | `FALL_THROUGH`
<a id="insn-00bbe408"></a> `00bbe408` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbe40c"></a> `00bbe40c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe410"></a> `00bbe410` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00bbe414"></a> `00bbe414` | `55 02 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe418"></a> `00bbe418` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe41c"></a> `00bbe41c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe420"></a> `00bbe420` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe424"></a> `00bbe424` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe428"></a> `00bbe428` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe42c"></a> `00bbe42c` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe430"></a> `00bbe430` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe434"></a> `00bbe434` | `08 01 00 54` | b.hi 0x00bbe454 | `CONDITIONAL_JUMP`
<a id="insn-00bbe438"></a> `00bbe438` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe43c"></a> `00bbe43c` | `65 7b 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe440"></a> `00bbe440` | `60 6d 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe444"></a> `00bbe444` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe448"></a> `00bbe448` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe44c"></a> `00bbe44c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe450"></a> `00bbe450` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe454"></a> `00bbe454` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe458"></a> `00bbe458` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe45c"></a> `00bbe45c` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe460"></a> `00bbe460` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe464"></a> `00bbe464` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe468"></a> `00bbe468` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe46c"></a> `00bbe46c` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe470"></a> `00bbe470` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe474"></a> `00bbe474` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe478"></a> `00bbe478` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbe47c"></a> `00bbe47c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe480"></a> `00bbe480` | `89 b6 ff f0` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00bbe484"></a> `00bbe484` | `29 19 20 91` | add x9,x9,#0x806 | `FALL_THROUGH`
<a id="insn-00bbe488"></a> `00bbe488` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbe48c"></a> `00bbe48c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe490"></a> `00bbe490` | `48 01 80 52` | mov w8,#0xa | `FALL_THROUGH`
<a id="insn-00bbe494"></a> `00bbe494` | `35 02 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe498"></a> `00bbe498` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe49c"></a> `00bbe49c` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe4a0"></a> `00bbe4a0` | `bf 0f 00 f9` | str xzr,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbe4a4"></a> `00bbe4a4` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bbe4a8"></a> `00bbe4a8` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbe4ac"></a> `00bbe4ac` | `e0 4a 00 54` | b.eq 0x00bbee08 | `CONDITIONAL_JUMP`
<a id="insn-00bbe4b0"></a> `00bbe4b0` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bbe4b4"></a> `00bbe4b4` | `4a e9 00 51` | sub w10,w10,#0x3a | `FALL_THROUGH`
<a id="insn-00bbe4b8"></a> `00bbe4b8` | `5f 29 00 31` | cmn w10,#0xa | `FALL_THROUGH`
<a id="insn-00bbe4bc"></a> `00bbe4bc` | `e2 4b 00 54` | b.cs 0x00bbee38 | `CONDITIONAL_JUMP`
<a id="insn-00bbe4c0"></a> `00bbe4c0` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bbe4c4"></a> `00bbe4c4` | `3f 7d 01 71` | cmp w9,#0x5f | `FALL_THROUGH`
<a id="insn-00bbe4c8"></a> `00bbe4c8` | `01 4a 00 54` | b.ne 0x00bbee08 | `CONDITIONAL_JUMP`
<a id="insn-00bbe4cc"></a> `00bbe4cc` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbe4d0"></a> `00bbe4d0` | `69 02 00 14` | b 0x00bbee74 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe4d4"></a> `00bbe4d4` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe4d8"></a> `00bbe4d8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe4dc"></a> `00bbe4dc` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe4e0"></a> `00bbe4e0` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe4e4"></a> `00bbe4e4` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe4e8"></a> `00bbe4e8` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe4ec"></a> `00bbe4ec` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe4f0"></a> `00bbe4f0` | `08 01 00 54` | b.hi 0x00bbe510 | `CONDITIONAL_JUMP`
<a id="insn-00bbe4f4"></a> `00bbe4f4` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe4f8"></a> `00bbe4f8` | `36 7b 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe4fc"></a> `00bbe4fc` | `80 67 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe500"></a> `00bbe500` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe504"></a> `00bbe504` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe508"></a> `00bbe508` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe50c"></a> `00bbe50c` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe510"></a> `00bbe510` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe514"></a> `00bbe514` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe518"></a> `00bbe518` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe51c"></a> `00bbe51c` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe520"></a> `00bbe520` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe524"></a> `00bbe524` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe528"></a> `00bbe528` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe52c"></a> `00bbe52c` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe530"></a> `00bbe530` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe534"></a> `00bbe534` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe538"></a> `00bbe538` | `89 b6 ff f0` | adrp x9,0x291000 | `FALL_THROUGH`
<a id="insn-00bbe53c"></a> `00bbe53c` | `29 d9 14 91` | add x9,x9,#0x536 | `FALL_THROUGH`
<a id="insn-00bbe540"></a> `00bbe540` | `06 02 00 14` | b 0x00bbed58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe544"></a> `00bbe544` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe548"></a> `00bbe548` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe54c"></a> `00bbe54c` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe550"></a> `00bbe550` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe554"></a> `00bbe554` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe558"></a> `00bbe558` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe55c"></a> `00bbe55c` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe560"></a> `00bbe560` | `08 01 00 54` | b.hi 0x00bbe580 | `CONDITIONAL_JUMP`
<a id="insn-00bbe564"></a> `00bbe564` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe568"></a> `00bbe568` | `1a 7b 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe56c"></a> `00bbe56c` | `00 64 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe570"></a> `00bbe570` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe574"></a> `00bbe574` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe578"></a> `00bbe578` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe57c"></a> `00bbe57c` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe580"></a> `00bbe580` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe584"></a> `00bbe584` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe588"></a> `00bbe588` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe58c"></a> `00bbe58c` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe590"></a> `00bbe590` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe594"></a> `00bbe594` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe598"></a> `00bbe598` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe59c"></a> `00bbe59c` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe5a0"></a> `00bbe5a0` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe5a4"></a> `00bbe5a4` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbe5a8"></a> `00bbe5a8` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe5ac"></a> `00bbe5ac` | `e9 b6 ff f0` | adrp x9,0x29d000 | `FALL_THROUGH`
<a id="insn-00bbe5b0"></a> `00bbe5b0` | `29 89 0a 91` | add x9,x9,#0x2a2 | `FALL_THROUGH`
<a id="insn-00bbe5b4"></a> `00bbe5b4` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbe5b8"></a> `00bbe5b8` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe5bc"></a> `00bbe5bc` | `28 02 80 52` | mov w8,#0x11 | `FALL_THROUGH`
<a id="insn-00bbe5c0"></a> `00bbe5c0` | `ea 01 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe5c4"></a> `00bbe5c4` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe5c8"></a> `00bbe5c8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe5cc"></a> `00bbe5cc` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe5d0"></a> `00bbe5d0` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe5d4"></a> `00bbe5d4` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe5d8"></a> `00bbe5d8` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe5dc"></a> `00bbe5dc` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe5e0"></a> `00bbe5e0` | `08 01 00 54` | b.hi 0x00bbe600 | `CONDITIONAL_JUMP`
<a id="insn-00bbe5e4"></a> `00bbe5e4` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe5e8"></a> `00bbe5e8` | `fa 7a 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe5ec"></a> `00bbe5ec` | `00 60 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe5f0"></a> `00bbe5f0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe5f4"></a> `00bbe5f4` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe5f8"></a> `00bbe5f8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe5fc"></a> `00bbe5fc` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe600"></a> `00bbe600` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe604"></a> `00bbe604` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe608"></a> `00bbe608` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe60c"></a> `00bbe60c` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe610"></a> `00bbe610` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe614"></a> `00bbe614` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe618"></a> `00bbe618` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe61c"></a> `00bbe61c` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe620"></a> `00bbe620` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe624"></a> `00bbe624` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe628"></a> `00bbe628` | `09 b7 ff d0` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-00bbe62c"></a> `00bbe62c` | `29 f9 3e 91` | add x9,x9,#0xfbe | `FALL_THROUGH`
<a id="insn-00bbe630"></a> `00bbe630` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbe634"></a> `00bbe634` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbe638"></a> `00bbe638` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe63c"></a> `00bbe63c` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bbe640"></a> `00bbe640` | `ca 01 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe644"></a> `00bbe644` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe648"></a> `00bbe648` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe64c"></a> `00bbe64c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe650"></a> `00bbe650` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe654"></a> `00bbe654` | `02 fe ff 97` | bl 0x00bbde5c | `UNCONDITIONAL_CALL`
<a id="insn-00bbe658"></a> `00bbe658` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe65c"></a> `00bbe65c` | `80 38 00 b4` | cbz x0,0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbe660"></a> `00bbe660` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbe664"></a> `00bbe664` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe668"></a> `00bbe668` | `c1 4f 00 94` | bl 0x00bd256c | `UNCONDITIONAL_CALL`
<a id="insn-00bbe66c"></a> `00bbe66c` | `8c 00 00 14` | b 0x00bbe89c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe670"></a> `00bbe670` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe674"></a> `00bbe674` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe678"></a> `00bbe678` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe67c"></a> `00bbe67c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe680"></a> `00bbe680` | `f7 fd ff 97` | bl 0x00bbde5c | `UNCONDITIONAL_CALL`
<a id="insn-00bbe684"></a> `00bbe684` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe688"></a> `00bbe688` | `20 37 00 b4` | cbz x0,0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbe68c"></a> `00bbe68c` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbe690"></a> `00bbe690` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe694"></a> `00bbe694` | `e2 4f 00 94` | bl 0x00bd261c | `UNCONDITIONAL_CALL`
<a id="insn-00bbe698"></a> `00bbe698` | `81 00 00 14` | b 0x00bbe89c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe69c"></a> `00bbe69c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe6a0"></a> `00bbe6a0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe6a4"></a> `00bbe6a4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe6a8"></a> `00bbe6a8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe6ac"></a> `00bbe6ac` | `ec fd ff 97` | bl 0x00bbde5c | `UNCONDITIONAL_CALL`
<a id="insn-00bbe6b0"></a> `00bbe6b0` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe6b4"></a> `00bbe6b4` | `20 0f 00 b4` | cbz x0,0x00bbe898 | `CONDITIONAL_JUMP`
<a id="insn-00bbe6b8"></a> `00bbe6b8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe6bc"></a> `00bbe6bc` | `e8 fd ff 97` | bl 0x00bbde5c | `UNCONDITIONAL_CALL`
<a id="insn-00bbe6c0"></a> `00bbe6c0` | `a0 0f 00 f9` | str x0,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbe6c4"></a> `00bbe6c4` | `a0 0e 00 b4` | cbz x0,0x00bbe898 | `CONDITIONAL_JUMP`
<a id="insn-00bbe6c8"></a> `00bbe6c8` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbe6cc"></a> `00bbe6cc` | `a2 63 00 91` | add x2,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe6d0"></a> `00bbe6d0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe6d4"></a> `00bbe6d4` | `4d 56 00 94` | bl 0x00bd4008 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe6d8"></a> `00bbe6d8` | `20 0e 00 b5` | cbnz x0,0x00bbe89c | `CONDITIONAL_JUMP`
<a id="insn-00bbe6dc"></a> `00bbe6dc` | `a4 01 00 14` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe6e0"></a> `00bbe6e0` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe6e4"></a> `00bbe6e4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe6e8"></a> `00bbe6e8` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe6ec"></a> `00bbe6ec` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe6f0"></a> `00bbe6f0` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe6f4"></a> `00bbe6f4` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe6f8"></a> `00bbe6f8` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe6fc"></a> `00bbe6fc` | `08 01 00 54` | b.hi 0x00bbe71c | `CONDITIONAL_JUMP`
<a id="insn-00bbe700"></a> `00bbe700` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe704"></a> `00bbe704` | `b3 7a 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe708"></a> `00bbe708` | `20 57 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe70c"></a> `00bbe70c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe710"></a> `00bbe710` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe714"></a> `00bbe714` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe718"></a> `00bbe718` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe71c"></a> `00bbe71c` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe720"></a> `00bbe720` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe724"></a> `00bbe724` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe728"></a> `00bbe728` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe72c"></a> `00bbe72c` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe730"></a> `00bbe730` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe734"></a> `00bbe734` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe738"></a> `00bbe738` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe73c"></a> `00bbe73c` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe740"></a> `00bbe740` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe744"></a> `00bbe744` | `e9 b6 ff d0` | adrp x9,0x29c000 | `FALL_THROUGH`
<a id="insn-00bbe748"></a> `00bbe748` | `29 25 3d 91` | add x9,x9,#0xf49 | `FALL_THROUGH`
<a id="insn-00bbe74c"></a> `00bbe74c` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbe750"></a> `00bbe750` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbe754"></a> `00bbe754` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe758"></a> `00bbe758` | `a8 00 80 52` | mov w8,#0x5 | `FALL_THROUGH`
<a id="insn-00bbe75c"></a> `00bbe75c` | `83 01 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe760"></a> `00bbe760` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe764"></a> `00bbe764` | `0b 05 00 91` | add x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe768"></a> `00bbe768` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bbe76c"></a> `00bbe76c` | `6b 02 00 f9` | str x11,[x19] | `FALL_THROUGH`
<a id="insn-00bbe770"></a> `00bbe770` | `a0 53 00 54` | b.eq 0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe774"></a> `00bbe774` | `6b 01 40 39` | ldrb w11,[x11] | `FALL_THROUGH`
<a id="insn-00bbe778"></a> `00bbe778` | `6b e9 00 51` | sub w11,w11,#0x3a | `FALL_THROUGH`
<a id="insn-00bbe77c"></a> `00bbe77c` | `7f 29 00 31` | cmn w11,#0xa | `FALL_THROUGH`
<a id="insn-00bbe780"></a> `00bbe780` | `23 53 00 54` | b.cc 0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe784"></a> `00bbe784` | `f1 03 1f aa` | mov x17,xzr | `FALL_THROUGH`
<a id="insn-00bbe788"></a> `00bbe788` | `ee 03 1f aa` | mov x14,xzr | `FALL_THROUGH`
<a id="insn-00bbe78c"></a> `00bbe78c` | `50 01 80 52` | mov w16,#0xa | `FALL_THROUGH`
<a id="insn-00bbe790"></a> `00bbe790` | `0d 01 11 8b` | add x13,x8,x17 | `FALL_THROUGH`
<a id="insn-00bbe794"></a> `00bbe794` | `ec 03 0e aa` | mov x12,x14 | `FALL_THROUGH`
<a id="insn-00bbe798"></a> `00bbe798` | `eb 03 11 aa` | mov x11,x17 | `FALL_THROUGH`
<a id="insn-00bbe79c"></a> `00bbe79c` | `af 09 00 91` | add x15,x13,#0x2 | `FALL_THROUGH`
<a id="insn-00bbe7a0"></a> `00bbe7a0` | `6f 02 00 f9` | str x15,[x19] | `FALL_THROUGH`
<a id="insn-00bbe7a4"></a> `00bbe7a4` | `ff 01 0a eb` | cmp x15,x10 | `FALL_THROUGH`
<a id="insn-00bbe7a8"></a> `00bbe7a8` | `ad 05 40 39` | ldrb w13,[x13, #0x1] | `FALL_THROUGH`
<a id="insn-00bbe7ac"></a> `00bbe7ac` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbe7b0"></a> `00bbe7b0` | `ce 35 10 9b` | madd x14,x14,x16,x13 | `FALL_THROUGH`
<a id="insn-00bbe7b4"></a> `00bbe7b4` | `ce c1 00 d1` | sub x14,x14,#0x30 | `FALL_THROUGH`
<a id="insn-00bbe7b8"></a> `00bbe7b8` | `c0 00 00 54` | b.eq 0x00bbe7d0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe7bc"></a> `00bbe7bc` | `f1 01 40 39` | ldrb w17,[x15] | `FALL_THROUGH`
<a id="insn-00bbe7c0"></a> `00bbe7c0` | `31 c2 00 51` | sub w17,w17,#0x30 | `FALL_THROUGH`
<a id="insn-00bbe7c4"></a> `00bbe7c4` | `3f 26 00 71` | cmp w17,#0x9 | `FALL_THROUGH`
<a id="insn-00bbe7c8"></a> `00bbe7c8` | `71 05 00 91` | add x17,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe7cc"></a> `00bbe7cc` | `29 fe ff 54` | b.ls 0x00bbe790 | `CONDITIONAL_JUMP`
<a id="insn-00bbe7d0"></a> `00bbe7d0` | `29 01 0b cb` | sub x9,x9,x11 | `FALL_THROUGH`
<a id="insn-00bbe7d4"></a> `00bbe7d4` | `29 09 00 d1` | sub x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bbe7d8"></a> `00bbe7d8` | `3f 01 0e eb` | cmp x9,x14 | `FALL_THROUGH`
<a id="insn-00bbe7dc"></a> `00bbe7dc` | `43 50 00 54` | b.cc 0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe7e0"></a> `00bbe7e0` | `49 01 80 52` | mov w9,#0xa | `FALL_THROUGH`
<a id="insn-00bbe7e4"></a> `00bbe7e4` | `10 01 0b 8b` | add x16,x8,x11 | `FALL_THROUGH`
<a id="insn-00bbe7e8"></a> `00bbe7e8` | `ef 3b 01 a9` | stp x15,x14,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbe7ec"></a> `00bbe7ec` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bbe7f0"></a> `00bbe7f0` | `89 35 09 9b` | madd x9,x12,x9,x13 | `FALL_THROUGH`
<a id="insn-00bbe7f4"></a> `00bbe7f4` | `09 02 09 8b` | add x9,x16,x9 | `FALL_THROUGH`
<a id="insn-00bbe7f8"></a> `00bbe7f8` | `29 b9 00 d1` | sub x9,x9,#0x2e | `FALL_THROUGH`
<a id="insn-00bbe7fc"></a> `00bbe7fc` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbe800"></a> `00bbe800` | `2e 4f 00 b4` | cbz x14,0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe804"></a> `00bbe804` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bbe808"></a> `00bbe808` | `80 35 00 54` | b.eq 0x00bbeeb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe80c"></a> `00bbe80c` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bbe810"></a> `00bbe810` | `3f 25 01 71` | cmp w9,#0x49 | `FALL_THROUGH`
<a id="insn-00bbe814"></a> `00bbe814` | `21 35 00 54` | b.ne 0x00bbeeb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe818"></a> `00bbe818` | `49 01 80 52` | mov w9,#0xa | `FALL_THROUGH`
<a id="insn-00bbe81c"></a> `00bbe81c` | `08 01 0b 8b` | add x8,x8,x11 | `FALL_THROUGH`
<a id="insn-00bbe820"></a> `00bbe820` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe824"></a> `00bbe824` | `89 35 09 9b` | madd x9,x12,x9,x13 | `FALL_THROUGH`
<a id="insn-00bbe828"></a> `00bbe828` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe82c"></a> `00bbe82c` | `08 b5 00 d1` | sub x8,x8,#0x2d | `FALL_THROUGH`
<a id="insn-00bbe830"></a> `00bbe830` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe834"></a> `00bbe834` | `8a fd ff 97` | bl 0x00bbde5c | `UNCONDITIONAL_CALL`
<a id="insn-00bbe838"></a> `00bbe838` | `a0 0f 00 f9` | str x0,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbe83c"></a> `00bbe83c` | `40 4d 00 b4` | cbz x0,0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe840"></a> `00bbe840` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbe844"></a> `00bbe844` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbe848"></a> `00bbe848` | `e0 4c 00 54` | b.eq 0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe84c"></a> `00bbe84c` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbe850"></a> `00bbe850` | `3f 15 01 71` | cmp w9,#0x45 | `FALL_THROUGH`
<a id="insn-00bbe854"></a> `00bbe854` | `81 4c 00 54` | b.ne 0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe858"></a> `00bbe858` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe85c"></a> `00bbe85c` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbe860"></a> `00bbe860` | `a2 63 00 91` | add x2,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bbe864"></a> `00bbe864` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe868"></a> `00bbe868` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe86c"></a> `00bbe86c` | `3a 4d 00 94` | bl 0x00bd1d54 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe870"></a> `00bbe870` | `0b 00 00 14` | b 0x00bbe89c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe874"></a> `00bbe874` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe878"></a> `00bbe878` | `3f 09 00 f1` | cmp x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bbe87c"></a> `00bbe87c` | `83 28 00 54` | b.cc 0x00bbed8c | `CONDITIONAL_JUMP`
<a id="insn-00bbe880"></a> `00bbe880` | `08 05 40 39` | ldrb w8,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bbe884"></a> `00bbe884` | `1f d1 01 71` | cmp w8,#0x74 | `FALL_THROUGH`
<a id="insn-00bbe888"></a> `00bbe888` | `21 28 00 54` | b.ne 0x00bbed8c | `CONDITIONAL_JUMP`
<a id="insn-00bbe88c"></a> `00bbe88c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe890"></a> `00bbe890` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe894"></a> `00bbe894` | `88 4e 00 94` | bl 0x00bd22b4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe898"></a> `00bbe898` | `a0 26 00 b4` | cbz x0,0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbe89c"></a> `00bbe89c` | `76 22 53 a9` | ldp x22,x8,[x19, #0x130] | `FALL_THROUGH`
<a id="insn-00bbe8a0"></a> `00bbe8a0` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bbe8a4"></a> `00bbe8a4` | `a1 03 00 54` | b.ne 0x00bbe918 | `CONDITIONAL_JUMP`
<a id="insn-00bbe8a8"></a> `00bbe8a8` | `75 96 40 f9` | ldr x21,[x19, #0x128] | `FALL_THROUGH`
<a id="insn-00bbe8ac"></a> `00bbe8ac` | `68 02 05 91` | add x8,x19,#0x140 | `FALL_THROUGH`
<a id="insn-00bbe8b0"></a> `00bbe8b0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbe8b4"></a> `00bbe8b4` | `d4 02 15 cb` | sub x20,x22,x21 | `FALL_THROUGH`
<a id="insn-00bbe8b8"></a> `00bbe8b8` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bbe8bc"></a> `00bbe8bc` | `81 fa 7f d3` | lsl x1,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe8c0"></a> `00bbe8c0` | `c0 00 00 54` | b.eq 0x00bbe8d8 | `CONDITIONAL_JUMP`
<a id="insn-00bbe8c4"></a> `00bbe8c4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbe8c8"></a> `00bbe8c8` | `62 7a 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe8cc"></a> `00bbe8cc` | `60 96 00 f9` | str x0,[x19, #0x128] | `FALL_THROUGH`
<a id="insn-00bbe8d0"></a> `00bbe8d0` | `a0 01 00 b5` | cbnz x0,0x00bbe904 | `CONDITIONAL_JUMP`
<a id="insn-00bbe8d4"></a> `00bbe8d4` | `7b 7e 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bbe8d8"></a> `00bbe8d8` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bbe8dc"></a> `00bbe8dc` | `3d 7a 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe8e0"></a> `00bbe8e0` | `80 48 00 b4` | cbz x0,0x00bbf1f0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe8e4"></a> `00bbe8e4` | `df 02 15 eb` | cmp x22,x21 | `FALL_THROUGH`
<a id="insn-00bbe8e8"></a> `00bbe8e8` | `c0 00 00 54` | b.eq 0x00bbe900 | `CONDITIONAL_JUMP`
<a id="insn-00bbe8ec"></a> `00bbe8ec` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbe8f0"></a> `00bbe8f0` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bbe8f4"></a> `00bbe8f4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbe8f8"></a> `00bbe8f8` | `fe 71 00 94` | bl 0x00bdb0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe8fc"></a> `00bbe8fc` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbe900"></a> `00bbe900` | `60 96 00 f9` | str x0,[x19, #0x128] | `FALL_THROUGH`
<a id="insn-00bbe904"></a> `00bbe904` | `88 fe 42 93` | asr x8,x20,#0x2 | `FALL_THROUGH`
<a id="insn-00bbe908"></a> `00bbe908` | `16 00 14 8b` | add x22,x0,x20 | `FALL_THROUGH`
<a id="insn-00bbe90c"></a> `00bbe90c` | `08 0c 08 8b` | add x8,x0,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bbe910"></a> `00bbe910` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbe914"></a> `00bbe914` | `68 9e 00 f9` | str x8,[x19, #0x138] | `FALL_THROUGH`
<a id="insn-00bbe918"></a> `00bbe918` | `c8 22 00 91` | add x8,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe91c"></a> `00bbe91c` | `68 9a 00 f9` | str x8,[x19, #0x130] | `FALL_THROUGH`
<a id="insn-00bbe920"></a> `00bbe920` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00bbe924"></a> `00bbe924` | `12 01 00 14` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe928"></a> `00bbe928` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe92c"></a> `00bbe92c` | `3f 09 00 f1` | cmp x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bbe930"></a> `00bbe930` | `a3 45 00 54` | b.cc 0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbe934"></a> `00bbe934` | `09 05 40 39` | ldrb w9,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bbe938"></a> `00bbe938` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbe93c"></a> `00bbe93c` | `2b 09 01 51` | sub w11,w9,#0x42 | `FALL_THROUGH`
<a id="insn-00bbe940"></a> `00bbe940` | `7f d9 00 71` | cmp w11,#0x36 | `FALL_THROUGH`
<a id="insn-00bbe944"></a> `00bbe944` | `48 21 00 54` | b.hi 0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbe948"></a> `00bbe948` | `ec b9 ff d0` | adrp x12,0x2fc000 | `FALL_THROUGH`
<a id="insn-00bbe94c"></a> `00bbe94c` | `8c 71 2f 91` | add x12,x12,#0xbdc | `FALL_THROUGH`
<a id="insn-00bbe950"></a> `00bbe950` | `8d 00 00 10` | adr x13,0xbbe960 | `FALL_THROUGH`
<a id="insn-00bbe954"></a> `00bbe954` | `8e 79 6b 78` | ldrh w14,[x12, x11, LSL #0x1] | `FALL_THROUGH`
<a id="insn-00bbe958"></a> `00bbe958` | `ad 09 0e 8b` | add x13,x13,x14, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bbe95c"></a> `00bbe95c` | `a0 01 1f d6` | br x13 | `COMPUTED_JUMP`
<a id="insn-00bbe960"></a> `00bbe960` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe964"></a> `00bbe964` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbe968"></a> `00bbe968` | `1a 4a 00 94` | bl 0x00bd11d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe96c"></a> `00bbe96c` | `80 f9 ff b5` | cbnz x0,0x00bbe89c | `CONDITIONAL_JUMP`
<a id="insn-00bbe970"></a> `00bbe970` | `ff 00 00 14` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe974"></a> `00bbe974` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe978"></a> `00bbe978` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe97c"></a> `00bbe97c` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe980"></a> `00bbe980` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbe984"></a> `00bbe984` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe988"></a> `00bbe988` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbe98c"></a> `00bbe98c` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbe990"></a> `00bbe990` | `08 01 00 54` | b.hi 0x00bbe9b0 | `CONDITIONAL_JUMP`
<a id="insn-00bbe994"></a> `00bbe994` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbe998"></a> `00bbe998` | `0e 7a 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbe99c"></a> `00bbe99c` | `80 42 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbe9a0"></a> `00bbe9a0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbe9a4"></a> `00bbe9a4` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbe9a8"></a> `00bbe9a8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbe9ac"></a> `00bbe9ac` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbe9b0"></a> `00bbe9b0` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbe9b4"></a> `00bbe9b4` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbe9b8"></a> `00bbe9b8` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbe9bc"></a> `00bbe9bc` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbe9c0"></a> `00bbe9c0` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe9c4"></a> `00bbe9c4` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbe9c8"></a> `00bbe9c8` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbe9cc"></a> `00bbe9cc` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe9d0"></a> `00bbe9d0` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbe9d4"></a> `00bbe9d4` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbe9d8"></a> `00bbe9d8` | `09 b7 ff d0` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-00bbe9dc"></a> `00bbe9dc` | `29 39 0d 91` | add x9,x9,#0x34e | `FALL_THROUGH`
<a id="insn-00bbe9e0"></a> `00bbe9e0` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbe9e4"></a> `00bbe9e4` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbe9e8"></a> `00bbe9e8` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbe9ec"></a> `00bbe9ec` | `a8 01 80 52` | mov w8,#0xd | `FALL_THROUGH`
<a id="insn-00bbe9f0"></a> `00bbe9f0` | `de 00 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbe9f4"></a> `00bbe9f4` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbe9f8"></a> `00bbe9f8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbe9fc"></a> `00bbe9fc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbea00"></a> `00bbea00` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbea04"></a> `00bbea04` | `16 fd ff 97` | bl 0x00bbde5c | `UNCONDITIONAL_CALL`
<a id="insn-00bbea08"></a> `00bbea08` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbea0c"></a> `00bbea0c` | `00 1b 00 b4` | cbz x0,0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbea10"></a> `00bbea10` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbea14"></a> `00bbea14` | `a8 1b 00 b9` | str w8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbea18"></a> `00bbea18` | `65 00 00 14` | b 0x00bbebac | `UNCONDITIONAL_JUMP`
<a id="insn-00bbea1c"></a> `00bbea1c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbea20"></a> `00bbea20` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbea24"></a> `00bbea24` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbea28"></a> `00bbea28` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbea2c"></a> `00bbea2c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbea30"></a> `00bbea30` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbea34"></a> `00bbea34` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbea38"></a> `00bbea38` | `08 01 00 54` | b.hi 0x00bbea58 | `CONDITIONAL_JUMP`
<a id="insn-00bbea3c"></a> `00bbea3c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbea40"></a> `00bbea40` | `e4 79 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbea44"></a> `00bbea44` | `40 3d 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbea48"></a> `00bbea48` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbea4c"></a> `00bbea4c` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbea50"></a> `00bbea50` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbea54"></a> `00bbea54` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbea58"></a> `00bbea58` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbea5c"></a> `00bbea5c` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbea60"></a> `00bbea60` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbea64"></a> `00bbea64` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbea68"></a> `00bbea68` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbea6c"></a> `00bbea6c` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbea70"></a> `00bbea70` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbea74"></a> `00bbea74` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbea78"></a> `00bbea78` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbea7c"></a> `00bbea7c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbea80"></a> `00bbea80` | `c9 b6 ff b0` | adrp x9,0x297000 | `FALL_THROUGH`
<a id="insn-00bbea84"></a> `00bbea84` | `29 21 21 91` | add x9,x9,#0x848 | `FALL_THROUGH`
<a id="insn-00bbea88"></a> `00bbea88` | `94 00 00 14` | b 0x00bbecd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbea8c"></a> `00bbea8c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbea90"></a> `00bbea90` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbea94"></a> `00bbea94` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbea98"></a> `00bbea98` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbea9c"></a> `00bbea9c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbeaa0"></a> `00bbeaa0` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbeaa4"></a> `00bbeaa4` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbeaa8"></a> `00bbeaa8` | `08 01 00 54` | b.hi 0x00bbeac8 | `CONDITIONAL_JUMP`
<a id="insn-00bbeaac"></a> `00bbeaac` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbeab0"></a> `00bbeab0` | `c8 79 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbeab4"></a> `00bbeab4` | `c0 39 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbeab8"></a> `00bbeab8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbeabc"></a> `00bbeabc` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbeac0"></a> `00bbeac0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbeac4"></a> `00bbeac4` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbeac8"></a> `00bbeac8` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbeacc"></a> `00bbeacc` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbead0"></a> `00bbead0` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbead4"></a> `00bbead4` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbead8"></a> `00bbead8` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbeadc"></a> `00bbeadc` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbeae0"></a> `00bbeae0` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbeae4"></a> `00bbeae4` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbeae8"></a> `00bbeae8` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbeaec"></a> `00bbeaec` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbeaf0"></a> `00bbeaf0` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbeaf4"></a> `00bbeaf4` | `49 b7 ff b0` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bbeaf8"></a> `00bbeaf8` | `29 2d 0c 91` | add x9,x9,#0x30b | `FALL_THROUGH`
<a id="insn-00bbeafc"></a> `00bbeafc` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbeb00"></a> `00bbeb00` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbeb04"></a> `00bbeb04` | `88 01 80 52` | mov w8,#0xc | `FALL_THROUGH`
<a id="insn-00bbeb08"></a> `00bbeb08` | `98 00 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeb0c"></a> `00bbeb0c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbeb10"></a> `00bbeb10` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbeb14"></a> `00bbeb14` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbeb18"></a> `00bbeb18` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbeb1c"></a> `00bbeb1c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbeb20"></a> `00bbeb20` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbeb24"></a> `00bbeb24` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbeb28"></a> `00bbeb28` | `08 01 00 54` | b.hi 0x00bbeb48 | `CONDITIONAL_JUMP`
<a id="insn-00bbeb2c"></a> `00bbeb2c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbeb30"></a> `00bbeb30` | `a8 79 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbeb34"></a> `00bbeb34` | `c0 35 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbeb38"></a> `00bbeb38` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbeb3c"></a> `00bbeb3c` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbeb40"></a> `00bbeb40` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbeb44"></a> `00bbeb44` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbeb48"></a> `00bbeb48` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbeb4c"></a> `00bbeb4c` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbeb50"></a> `00bbeb50` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbeb54"></a> `00bbeb54` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbeb58"></a> `00bbeb58` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbeb5c"></a> `00bbeb5c` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbeb60"></a> `00bbeb60` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbeb64"></a> `00bbeb64` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbeb68"></a> `00bbeb68` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbeb6c"></a> `00bbeb6c` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbeb70"></a> `00bbeb70` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbeb74"></a> `00bbeb74` | `89 b6 ff d0` | adrp x9,0x290000 | `FALL_THROUGH`
<a id="insn-00bbeb78"></a> `00bbeb78` | `29 e1 21 91` | add x9,x9,#0x878 | `FALL_THROUGH`
<a id="insn-00bbeb7c"></a> `00bbeb7c` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbeb80"></a> `00bbeb80` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbeb84"></a> `00bbeb84` | `c8 01 80 52` | mov w8,#0xe | `FALL_THROUGH`
<a id="insn-00bbeb88"></a> `00bbeb88` | `78 00 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeb8c"></a> `00bbeb8c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbeb90"></a> `00bbeb90` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbeb94"></a> `00bbeb94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbeb98"></a> `00bbeb98` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbeb9c"></a> `00bbeb9c` | `b0 fc ff 97` | bl 0x00bbde5c | `UNCONDITIONAL_CALL`
<a id="insn-00bbeba0"></a> `00bbeba0` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbeba4"></a> `00bbeba4` | `40 0e 00 b4` | cbz x0,0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbeba8"></a> `00bbeba8` | `bf 1b 00 b9` | str wzr,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbebac"></a> `00bbebac` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbebb0"></a> `00bbebb0` | `a2 63 00 91` | add x2,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bbebb4"></a> `00bbebb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbebb8"></a> `00bbebb8` | `3e 4e 00 94` | bl 0x00bd24b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbebbc"></a> `00bbebbc` | `38 ff ff 17` | b 0x00bbe89c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbebc0"></a> `00bbebc0` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbebc4"></a> `00bbebc4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbebc8"></a> `00bbebc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbebcc"></a> `00bbebcc` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbebd0"></a> `00bbebd0` | `a3 fc ff 97` | bl 0x00bbde5c | `UNCONDITIONAL_CALL`
<a id="insn-00bbebd4"></a> `00bbebd4` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbebd8"></a> `00bbebd8` | `a0 0c 00 b4` | cbz x0,0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbebdc"></a> `00bbebdc` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbebe0"></a> `00bbebe0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbebe4"></a> `00bbebe4` | `08 4e 00 94` | bl 0x00bd2404 | `UNCONDITIONAL_CALL`
<a id="insn-00bbebe8"></a> `00bbebe8` | `2d ff ff 17` | b 0x00bbe89c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbebec"></a> `00bbebec` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbebf0"></a> `00bbebf0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbebf4"></a> `00bbebf4` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbebf8"></a> `00bbebf8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbebfc"></a> `00bbebfc` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbec00"></a> `00bbec00` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbec04"></a> `00bbec04` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbec08"></a> `00bbec08` | `08 01 00 54` | b.hi 0x00bbec28 | `CONDITIONAL_JUMP`
<a id="insn-00bbec0c"></a> `00bbec0c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbec10"></a> `00bbec10` | `70 79 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbec14"></a> `00bbec14` | `c0 2e 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbec18"></a> `00bbec18` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbec1c"></a> `00bbec1c` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbec20"></a> `00bbec20` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbec24"></a> `00bbec24` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbec28"></a> `00bbec28` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbec2c"></a> `00bbec2c` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbec30"></a> `00bbec30` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbec34"></a> `00bbec34` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbec38"></a> `00bbec38` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbec3c"></a> `00bbec3c` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbec40"></a> `00bbec40` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbec44"></a> `00bbec44` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbec48"></a> `00bbec48` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbec4c"></a> `00bbec4c` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbec50"></a> `00bbec50` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbec54"></a> `00bbec54` | `49 b7 ff f0` | adrp x9,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bbec58"></a> `00bbec58` | `29 49 07 91` | add x9,x9,#0x1d2 | `FALL_THROUGH`
<a id="insn-00bbec5c"></a> `00bbec5c` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbec60"></a> `00bbec60` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbec64"></a> `00bbec64` | `28 01 80 52` | mov w8,#0x9 | `FALL_THROUGH`
<a id="insn-00bbec68"></a> `00bbec68` | `40 00 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbec6c"></a> `00bbec6c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbec70"></a> `00bbec70` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbec74"></a> `00bbec74` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbec78"></a> `00bbec78` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbec7c"></a> `00bbec7c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbec80"></a> `00bbec80` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbec84"></a> `00bbec84` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbec88"></a> `00bbec88` | `08 01 00 54` | b.hi 0x00bbeca8 | `CONDITIONAL_JUMP`
<a id="insn-00bbec8c"></a> `00bbec8c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbec90"></a> `00bbec90` | `50 79 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbec94"></a> `00bbec94` | `c0 2a 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbec98"></a> `00bbec98` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbec9c"></a> `00bbec9c` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbeca0"></a> `00bbeca0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbeca4"></a> `00bbeca4` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbeca8"></a> `00bbeca8` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbecac"></a> `00bbecac` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbecb0"></a> `00bbecb0` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbecb4"></a> `00bbecb4` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbecb8"></a> `00bbecb8` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbecbc"></a> `00bbecbc` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbecc0"></a> `00bbecc0` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbecc4"></a> `00bbecc4` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbecc8"></a> `00bbecc8` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbeccc"></a> `00bbeccc` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbecd0"></a> `00bbecd0` | `49 b7 ff f0` | adrp x9,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bbecd4"></a> `00bbecd4` | `29 19 07 91` | add x9,x9,#0x1c6 | `FALL_THROUGH`
<a id="insn-00bbecd8"></a> `00bbecd8` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbecdc"></a> `00bbecdc` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbece0"></a> `00bbece0` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbece4"></a> `00bbece4` | `68 01 80 52` | mov w8,#0xb | `FALL_THROUGH`
<a id="insn-00bbece8"></a> `00bbece8` | `20 00 00 14` | b 0x00bbed68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbecec"></a> `00bbecec` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbecf0"></a> `00bbecf0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbecf4"></a> `00bbecf4` | `74 9a 49 f9` | ldr x20,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbecf8"></a> `00bbecf8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbecfc"></a> `00bbecfc` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbed00"></a> `00bbed00` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbed04"></a> `00bbed04` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbed08"></a> `00bbed08` | `08 01 00 54` | b.hi 0x00bbed28 | `CONDITIONAL_JUMP`
<a id="insn-00bbed0c"></a> `00bbed0c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbed10"></a> `00bbed10` | `30 79 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbed14"></a> `00bbed14` | `c0 26 00 b4` | cbz x0,0x00bbf1ec | `CONDITIONAL_JUMP`
<a id="insn-00bbed18"></a> `00bbed18` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbed1c"></a> `00bbed1c` | `14 7c 00 a9` | stp x20,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbed20"></a> `00bbed20` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbed24"></a> `00bbed24` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbed28"></a> `00bbed28` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbed2c"></a> `00bbed2c` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00bbed30"></a> `00bbed30` | `c8 02 00 b0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bbed34"></a> `00bbed34` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bbed38"></a> `00bbed38` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbed3c"></a> `00bbed3c` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bbed40"></a> `00bbed40` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbed44"></a> `00bbed44` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbed48"></a> `00bbed48` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbed4c"></a> `00bbed4c` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbed50"></a> `00bbed50` | `09 b7 ff f0` | adrp x9,0x2a1000 | `FALL_THROUGH`
<a id="insn-00bbed54"></a> `00bbed54` | `29 7d 09 91` | add x9,x9,#0x25f | `FALL_THROUGH`
<a id="insn-00bbed58"></a> `00bbed58` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbed5c"></a> `00bbed5c` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbed60"></a> `00bbed60` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbed64"></a> `00bbed64` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bbed68"></a> `00bbed68` | `09 20 01 a9` | stp x9,x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbed6c"></a> `00bbed6c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbed70"></a> `00bbed70` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbed74"></a> `00bbed74` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbed78"></a> `00bbed78` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbed7c"></a> `00bbed7c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbed80"></a> `00bbed80` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbed84"></a> `00bbed84` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbed88"></a> `00bbed88` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbed8c"></a> `00bbed8c` | `a2 63 00 91` | add x2,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bbed90"></a> `00bbed90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbed94"></a> `00bbed94` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbed98"></a> `00bbed98` | `bf 63 00 39` | strb wzr,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbed9c"></a> `00bbed9c` | `12 0a 00 94` | bl 0x00bc15e4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbeda0"></a> `00bbeda0` | `e0 07 00 f9` | str x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbeda4"></a> `00bbeda4` | `00 22 00 b4` | cbz x0,0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbeda8"></a> `00bbeda8` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbedac"></a> `00bbedac` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbedb0"></a> `00bbedb0` | `e0 07 00 54` | b.eq 0x00bbeeac | `CONDITIONAL_JUMP`
<a id="insn-00bbedb4"></a> `00bbedb4` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbedb8"></a> `00bbedb8` | `a8 63 40 39` | ldrb w8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbedbc"></a> `00bbedbc` | `3f 25 01 71` | cmp w9,#0x49 | `FALL_THROUGH`
<a id="insn-00bbedc0"></a> `00bbedc0` | `81 07 00 54` | b.ne 0x00bbeeb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbedc4"></a> `00bbedc4` | `68 00 00 34` | cbz w8,0x00bbedd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbedc8"></a> `00bbedc8` | `69 22 4c 39` | ldrb w9,[x19, #0x308] | `FALL_THROUGH`
<a id="insn-00bbedcc"></a> `00bbedcc` | `09 fd ff 34` | cbz w9,0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbedd0"></a> `00bbedd0` | `88 00 00 35` | cbnz w8,0x00bbede0 | `CONDITIONAL_JUMP`
<a id="insn-00bbedd4"></a> `00bbedd4` | `60 a2 04 91` | add x0,x19,#0x128 | `FALL_THROUGH`
<a id="insn-00bbedd8"></a> `00bbedd8` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbeddc"></a> `00bbeddc` | `07 04 00 94` | bl 0x00bbfdf8 | `UNCONDITIONAL_CALL`
<a id="insn-00bbede0"></a> `00bbede0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbede4"></a> `00bbede4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbede8"></a> `00bbede8` | `5b 0a 00 94` | bl 0x00bc1754 | `UNCONDITIONAL_CALL`
<a id="insn-00bbedec"></a> `00bbedec` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbedf0"></a> `00bbedf0` | `a0 1f 00 b4` | cbz x0,0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbedf4"></a> `00bbedf4` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbedf8"></a> `00bbedf8` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbedfc"></a> `00bbedfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbee00"></a> `00bbee00` | `89 0b 00 94` | bl 0x00bc1c24 | `UNCONDITIONAL_CALL`
<a id="insn-00bbee04"></a> `00bbee04` | `a6 fe ff 17` | b 0x00bbe89c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbee08"></a> `00bbee08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbee0c"></a> `00bbee0c` | `40 10 00 94` | bl 0x00bc2f0c | `UNCONDITIONAL_CALL`
<a id="insn-00bbee10"></a> `00bbee10` | `40 d4 ff b4` | cbz x0,0x00bbe898 | `CONDITIONAL_JUMP`
<a id="insn-00bbee14"></a> `00bbee14` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbee18"></a> `00bbee18` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbee1c"></a> `00bbee1c` | `20 04 00 54` | b.eq 0x00bbeea0 | `CONDITIONAL_JUMP`
<a id="insn-00bbee20"></a> `00bbee20` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbee24"></a> `00bbee24` | `3f 7d 01 71` | cmp w9,#0x5f | `FALL_THROUGH`
<a id="insn-00bbee28"></a> `00bbee28` | `c1 03 00 54` | b.ne 0x00bbeea0 | `CONDITIONAL_JUMP`
<a id="insn-00bbee2c"></a> `00bbee2c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbee30"></a> `00bbee30` | `a0 0f 00 f9` | str x0,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbee34"></a> `00bbee34` | `10 00 00 14` | b 0x00bbee74 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbee38"></a> `00bbee38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbee3c"></a> `00bbee3c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbee40"></a> `00bbee40` | `b7 fb ff 97` | bl 0x00bbdd1c | `UNCONDITIONAL_CALL`
<a id="insn-00bbee44"></a> `00bbee44` | `e0 07 01 a9` | stp x0,x1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbee48"></a> `00bbee48` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbee4c"></a> `00bbee4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbee50"></a> `00bbee50` | `04 0f 00 94` | bl 0x00bc2a60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbee54"></a> `00bbee54` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbee58"></a> `00bbee58` | `a0 0f 00 f9` | str x0,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbee5c"></a> `00bbee5c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbee60"></a> `00bbee60` | `00 02 00 54` | b.eq 0x00bbeea0 | `CONDITIONAL_JUMP`
<a id="insn-00bbee64"></a> `00bbee64` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbee68"></a> `00bbee68` | `3f 7d 01 71` | cmp w9,#0x5f | `FALL_THROUGH`
<a id="insn-00bbee6c"></a> `00bbee6c` | `a1 01 00 54` | b.ne 0x00bbeea0 | `CONDITIONAL_JUMP`
<a id="insn-00bbee70"></a> `00bbee70` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbee74"></a> `00bbee74` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbee78"></a> `00bbee78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbee7c"></a> `00bbee7c` | `f8 fb ff 97` | bl 0x00bbde5c | `UNCONDITIONAL_CALL`
<a id="insn-00bbee80"></a> `00bbee80` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbee84"></a> `00bbee84` | `a0 d0 ff b4` | cbz x0,0x00bbe898 | `CONDITIONAL_JUMP`
<a id="insn-00bbee88"></a> `00bbee88` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbee8c"></a> `00bbee8c` | `a2 63 00 91` | add x2,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bbee90"></a> `00bbee90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbee94"></a> `00bbee94` | `be 53 00 94` | bl 0x00bd3d8c | `UNCONDITIONAL_CALL`
<a id="insn-00bbee98"></a> `00bbee98` | `20 d0 ff b5` | cbnz x0,0x00bbe89c | `CONDITIONAL_JUMP`
<a id="insn-00bbee9c"></a> `00bbee9c` | `b4 ff ff 17` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeea0"></a> `00bbeea0` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbeea4"></a> `00bbeea4` | `df cf ff b5` | cbnz xzr,0x00bbe89c | `CONDITIONAL_JUMP`
<a id="insn-00bbeea8"></a> `00bbeea8` | `b1 ff ff 17` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeeac"></a> `00bbeeac` | `a8 63 40 39` | ldrb w8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbeeb0"></a> `00bbeeb0` | `e8 f5 ff 35` | cbnz w8,0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbeeb4"></a> `00bbeeb4` | `7a fe ff 17` | b 0x00bbe89c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeeb8"></a> `00bbeeb8` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbeebc"></a> `00bbeebc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbeec0"></a> `00bbeec0` | `2b 09 00 94` | bl 0x00bc136c | `UNCONDITIONAL_CALL`
<a id="insn-00bbeec4"></a> `00bbeec4` | `76 fe ff 17` | b 0x00bbe89c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeec8"></a> `00bbeec8` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbeecc"></a> `00bbeecc` | `8a b6 ff d0` | adrp x10,0x290000 | `FALL_THROUGH`
<a id="insn-00bbeed0"></a> `00bbeed0` | `4a 69 22 91` | add x10,x10,#0x89a | `FALL_THROUGH`
<a id="insn-00bbeed4"></a> `00bbeed4` | `6b b7 ff d0` | adrp x11,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bbeed8"></a> `00bbeed8` | `6b fd 17 91` | add x11,x11,#0x5ff | `FALL_THROUGH`
<a id="insn-00bbeedc"></a> `00bbeedc` | `3f ad 01 71` | cmp w9,#0x6b | `FALL_THROUGH`
<a id="insn-00bbeee0"></a> `00bbeee0` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbeee4"></a> `00bbeee4` | `69 01 8a 9a` | csel x9,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bbeee8"></a> `00bbeee8` | `ea 01 80 52` | mov w10,#0xf | `FALL_THROUGH`
<a id="insn-00bbeeec"></a> `00bbeeec` | `ab 00 80 52` | mov w11,#0x5 | `FALL_THROUGH`
<a id="insn-00bbeef0"></a> `00bbeef0` | `6a 01 8a 9a` | csel x10,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00bbeef4"></a> `00bbeef4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbeef8"></a> `00bbeef8` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbeefc"></a> `00bbeefc` | `e9 2b 01 a9` | stp x9,x10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbef00"></a> `00bbef00` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbef04"></a> `00bbef04` | `26 01 00 94` | bl 0x00bbf39c | `UNCONDITIONAL_CALL`
<a id="insn-00bbef08"></a> `00bbef08` | `a0 0f 00 f9` | str x0,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbef0c"></a> `00bbef0c` | `00 f3 ff b4` | cbz x0,0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbef10"></a> `00bbef10` | `a1 63 00 91` | add x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bbef14"></a> `00bbef14` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbef18"></a> `00bbef18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbef1c"></a> `00bbef1c` | `0c 4c 00 94` | bl 0x00bd1f4c | `UNCONDITIONAL_CALL`
<a id="insn-00bbef20"></a> `00bbef20` | `93 ff ff 17` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbef24"></a> `00bbef24` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbef28"></a> `00bbef28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbef2c"></a> `00bbef2c` | `59 0c 00 94` | bl 0x00bc2090 | `UNCONDITIONAL_CALL`
<a id="insn-00bbef30"></a> `00bbef30` | `60 cb ff b5` | cbnz x0,0x00bbe89c | `CONDITIONAL_JUMP`
<a id="insn-00bbef34"></a> `00bbef34` | `8e ff ff 17` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbef38"></a> `00bbef38` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbef3c"></a> `00bbef3c` | `3f 09 01 71` | cmp w9,#0x42 | `FALL_THROUGH`
<a id="insn-00bbef40"></a> `00bbef40` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbef44"></a> `00bbef44` | `e9 17 9f 1a` | cset w9,eq | `FALL_THROUGH`
<a id="insn-00bbef48"></a> `00bbef48` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00bbef4c"></a> `00bbef4c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbef50"></a> `00bbef50` | `a9 63 00 39` | strb w9,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bbef54"></a> `00bbef54` | `a0 00 00 54` | b.eq 0x00bbef68 | `CONDITIONAL_JUMP`
<a id="insn-00bbef58"></a> `00bbef58` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bbef5c"></a> `00bbef5c` | `08 e9 00 51` | sub w8,w8,#0x3a | `FALL_THROUGH`
<a id="insn-00bbef60"></a> `00bbef60` | `1f 29 00 31` | cmn w8,#0xa | `FALL_THROUGH`
<a id="insn-00bbef64"></a> `00bbef64` | `62 11 00 54` | b.cs 0x00bbf190 | `CONDITIONAL_JUMP`
<a id="insn-00bbef68"></a> `00bbef68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbef6c"></a> `00bbef6c` | `e8 0f 00 94` | bl 0x00bc2f0c | `UNCONDITIONAL_CALL`
<a id="insn-00bbef70"></a> `00bbef70` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbef74"></a> `00bbef74` | `e0 11 00 b5` | cbnz x0,0x00bbf1b0 | `CONDITIONAL_JUMP`
<a id="insn-00bbef78"></a> `00bbef78` | `7d ff ff 17` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbef7c"></a> `00bbef7c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbef80"></a> `00bbef80` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbef84"></a> `00bbef84` | `a1 b6 ff f0` | adrp x1,0x295000 | `FALL_THROUGH`
<a id="insn-00bbef88"></a> `00bbef88` | `21 24 1e 91` | add x1,x1,#0x789 | `FALL_THROUGH`
<a id="insn-00bbef8c"></a> `00bbef8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbef90"></a> `00bbef90` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbef94"></a> `00bbef94` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbef98"></a> `00bbef98` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbef9c"></a> `00bbef9c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbefa0"></a> `00bbefa0` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbefa4"></a> `00bbefa4` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbefa8"></a> `00bbefa8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbefac"></a> `00bbefac` | `96 29 00 14` | b 0x00bc9604 | `CALL_TERMINATOR`
<a id="insn-00bbefb0"></a> `00bbefb0` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbefb4"></a> `00bbefb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbefb8"></a> `00bbefb8` | `10 4c 00 94` | bl 0x00bd1ff8 | `UNCONDITIONAL_CALL`
<a id="insn-00bbefbc"></a> `00bbefbc` | `00 c7 ff b5` | cbnz x0,0x00bbe89c | `CONDITIONAL_JUMP`
<a id="insn-00bbefc0"></a> `00bbefc0` | `6b ff ff 17` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbefc4"></a> `00bbefc4` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbefc8"></a> `00bbefc8` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbefcc"></a> `00bbefcc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbefd0"></a> `00bbefd0` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbefd4"></a> `00bbefd4` | `a2 fb ff 97` | bl 0x00bbde5c | `UNCONDITIONAL_CALL`
<a id="insn-00bbefd8"></a> `00bbefd8` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbefdc"></a> `00bbefdc` | `80 ec ff b4` | cbz x0,0x00bbed6c | `CONDITIONAL_JUMP`
<a id="insn-00bbefe0"></a> `00bbefe0` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbefe4"></a> `00bbefe4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbefe8"></a> `00bbefe8` | `e3 1c 00 94` | bl 0x00bc6374 | `UNCONDITIONAL_CALL`
<a id="insn-00bbefec"></a> `00bbefec` | `2c fe ff 17` | b 0x00bbe89c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbeff0"></a> `00bbeff0` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbeff4"></a> `00bbeff4` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbeff8"></a> `00bbeff8` | `e1 b6 ff 90` | adrp x1,0x29a000 | `FALL_THROUGH`
<a id="insn-00bbeffc"></a> `00bbeffc` | `21 fc 2b 91` | add x1,x1,#0xaff | `FALL_THROUGH`
<a id="insn-00bbf000"></a> `00bbf000` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbf004"></a> `00bbf004` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbf008"></a> `00bbf008` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbf00c"></a> `00bbf00c` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbf010"></a> `00bbf010` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbf014"></a> `00bbf014` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf018"></a> `00bbf018` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbf01c"></a> `00bbf01c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbf020"></a> `00bbf020` | `22 4b 00 14` | b 0x00bd1ca8 | `CALL_TERMINATOR`
<a id="insn-00bbf024"></a> `00bbf024` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbf028"></a> `00bbf028` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbf02c"></a> `00bbf02c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbf030"></a> `00bbf030` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbf034"></a> `00bbf034` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbf038"></a> `00bbf038` | `39 fb ff 97` | bl 0x00bbdd1c | `UNCONDITIONAL_CALL`
<a id="insn-00bbf03c"></a> `00bbf03c` | `e0 07 01 a9` | stp x0,x1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbf040"></a> `00bbf040` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbf044"></a> `00bbf044` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbf048"></a> `00bbf048` | `86 0e 00 94` | bl 0x00bc2a60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf04c"></a> `00bbf04c` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbf050"></a> `00bbf050` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbf054"></a> `00bbf054` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf058"></a> `00bbf058` | `60 0c 00 54` | b.eq 0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf05c"></a> `00bbf05c` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf060"></a> `00bbf060` | `3f 7d 01 71` | cmp w9,#0x5f | `FALL_THROUGH`
<a id="insn-00bbf064"></a> `00bbf064` | `01 0c 00 54` | b.ne 0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf068"></a> `00bbf068` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf06c"></a> `00bbf06c` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbf070"></a> `00bbf070` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbf074"></a> `00bbf074` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbf078"></a> `00bbf078` | `62 4b 00 94` | bl 0x00bd1e00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf07c"></a> `00bbf07c` | `3c ff ff 17` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf080"></a> `00bbf080` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbf084"></a> `00bbf084` | `21 b7 ff d0` | adrp x1,0x2a5000 | `FALL_THROUGH`
<a id="insn-00bbf088"></a> `00bbf088` | `21 7c 0d 91` | add x1,x1,#0x35f | `FALL_THROUGH`
<a id="insn-00bbf08c"></a> `00bbf08c` | `0c 00 00 14` | b 0x00bbf0bc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf090"></a> `00bbf090` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbf094"></a> `00bbf094` | `01 b7 ff d0` | adrp x1,0x2a1000 | `FALL_THROUGH`
<a id="insn-00bbf098"></a> `00bbf098` | `21 f4 09 91` | add x1,x1,#0x27d | `FALL_THROUGH`
<a id="insn-00bbf09c"></a> `00bbf09c` | `22 00 00 14` | b 0x00bbf124 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf0a0"></a> `00bbf0a0` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbf0a4"></a> `00bbf0a4` | `41 b7 ff d0` | adrp x1,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bbf0a8"></a> `00bbf0a8` | `21 98 07 91` | add x1,x1,#0x1e6 | `FALL_THROUGH`
<a id="insn-00bbf0ac"></a> `00bbf0ac` | `11 00 00 14` | b 0x00bbf0f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf0b0"></a> `00bbf0b0` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbf0b4"></a> `00bbf0b4` | `41 b7 ff d0` | adrp x1,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bbf0b8"></a> `00bbf0b8` | `21 70 07 91` | add x1,x1,#0x1dc | `FALL_THROUGH`
<a id="insn-00bbf0bc"></a> `00bbf0bc` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbf0c0"></a> `00bbf0c0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbf0c4"></a> `00bbf0c4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbf0c8"></a> `00bbf0c8` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbf0cc"></a> `00bbf0cc` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbf0d0"></a> `00bbf0d0` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbf0d4"></a> `00bbf0d4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf0d8"></a> `00bbf0d8` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbf0dc"></a> `00bbf0dc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbf0e0"></a> `00bbf0e0` | `9c 4a 00 14` | b 0x00bd1b50 | `CALL_TERMINATOR`
<a id="insn-00bbf0e4"></a> `00bbf0e4` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbf0e8"></a> `00bbf0e8` | `81 b6 ff f0` | adrp x1,0x292000 | `FALL_THROUGH`
<a id="insn-00bbf0ec"></a> `00bbf0ec` | `21 f0 16 91` | add x1,x1,#0x5bc | `FALL_THROUGH`
<a id="insn-00bbf0f0"></a> `00bbf0f0` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbf0f4"></a> `00bbf0f4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbf0f8"></a> `00bbf0f8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbf0fc"></a> `00bbf0fc` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbf100"></a> `00bbf100` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbf104"></a> `00bbf104` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbf108"></a> `00bbf108` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf10c"></a> `00bbf10c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbf110"></a> `00bbf110` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbf114"></a> `00bbf114` | `b1 0e 00 14` | b 0x00bc2bd8 | `CALL_TERMINATOR`
<a id="insn-00bbf118"></a> `00bbf118` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbf11c"></a> `00bbf11c` | `81 b7 ff 90` | adrp x1,0x2af000 | `FALL_THROUGH`
<a id="insn-00bbf120"></a> `00bbf120` | `21 f0 1f 91` | add x1,x1,#0x7fc | `FALL_THROUGH`
<a id="insn-00bbf124"></a> `00bbf124` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbf128"></a> `00bbf128` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbf12c"></a> `00bbf12c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbf130"></a> `00bbf130` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbf134"></a> `00bbf134` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbf138"></a> `00bbf138` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbf13c"></a> `00bbf13c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf140"></a> `00bbf140` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbf144"></a> `00bbf144` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbf148"></a> `00bbf148` | `ad 4a 00 14` | b 0x00bd1bfc | `CALL_TERMINATOR`
<a id="insn-00bbf14c"></a> `00bbf14c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbf150"></a> `00bbf150` | `81 b6 ff d0` | adrp x1,0x291000 | `FALL_THROUGH`
<a id="insn-00bbf154"></a> `00bbf154` | `21 44 20 91` | add x1,x1,#0x811 | `FALL_THROUGH`
<a id="insn-00bbf158"></a> `00bbf158` | `04 00 00 14` | b 0x00bbf168 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf15c"></a> `00bbf15c` | `9f 24 03 d5` | bti j | `FALL_THROUGH`
<a id="insn-00bbf160"></a> `00bbf160` | `a1 b6 ff d0` | adrp x1,0x295000 | `FALL_THROUGH`
<a id="insn-00bbf164"></a> `00bbf164` | `21 44 1e 91` | add x1,x1,#0x791 | `FALL_THROUGH`
<a id="insn-00bbf168"></a> `00bbf168` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbf16c"></a> `00bbf16c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbf170"></a> `00bbf170` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbf174"></a> `00bbf174` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbf178"></a> `00bbf178` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbf17c"></a> `00bbf17c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbf180"></a> `00bbf180` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbf184"></a> `00bbf184` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbf188"></a> `00bbf188` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbf18c"></a> `00bbf18c` | `3d 44 00 14` | b 0x00bd0280 | `CALL_TERMINATOR`
<a id="insn-00bbf190"></a> `00bbf190` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbf194"></a> `00bbf194` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbf198"></a> `00bbf198` | `e1 fa ff 97` | bl 0x00bbdd1c | `UNCONDITIONAL_CALL`
<a id="insn-00bbf19c"></a> `00bbf19c` | `e0 07 01 a9` | stp x0,x1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbf1a0"></a> `00bbf1a0` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbf1a4"></a> `00bbf1a4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbf1a8"></a> `00bbf1a8` | `2e 0e 00 94` | bl 0x00bc2a60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf1ac"></a> `00bbf1ac` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbf1b0"></a> `00bbf1b0` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbf1b4"></a> `00bbf1b4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbf1b8"></a> `00bbf1b8` | `60 01 00 54` | b.eq 0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf1bc"></a> `00bbf1bc` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbf1c0"></a> `00bbf1c0` | `3f 7d 01 71` | cmp w9,#0x5f | `FALL_THROUGH`
<a id="insn-00bbf1c4"></a> `00bbf1c4` | `01 01 00 54` | b.ne 0x00bbf1e4 | `CONDITIONAL_JUMP`
<a id="insn-00bbf1c8"></a> `00bbf1c8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbf1cc"></a> `00bbf1cc` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbf1d0"></a> `00bbf1d0` | `a2 63 00 91` | add x2,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bbf1d4"></a> `00bbf1d4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbf1d8"></a> `00bbf1d8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbf1dc"></a> `00bbf1dc` | `31 4b 00 94` | bl 0x00bd1ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbf1e0"></a> `00bbf1e0` | `e3 fe ff 17` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf1e4"></a> `00bbf1e4` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbf1e8"></a> `00bbf1e8` | `e1 fe ff 17` | b 0x00bbed6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbf1ec"></a> `00bbf1ec` | `f9 6f 00 94` | bl 0x00bdb1d0 | `CALL_TERMINATOR`
<a id="insn-00bbf1f0"></a> `00bbf1f0` | `34 7c 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbde5c`](#insn-00bbde5c) 範囲 `[['00bbde5c', '00bbde8b']]`
  - `CONDITIONAL_JUMP` [`00bbde88`](#insn-00bbde88) → [`00bbe88c`](#insn-00bbe88c)
  - `FALL_THROUGH` [`00bbde88`](#insn-00bbde88) → [`00bbde8c`](#insn-00bbde8c)
- ブロック [`00bbde8c`](#insn-00bbde8c) 範囲 `[['00bbde8c', '00bbde9b']]`
  - `CONDITIONAL_JUMP` [`00bbde98`](#insn-00bbde98) → [`00bbe88c`](#insn-00bbe88c)
  - `FALL_THROUGH` [`00bbde98`](#insn-00bbde98) → [`00bbde9c`](#insn-00bbde9c)
- ブロック [`00bbde9c`](#insn-00bbde9c) 範囲 `[['00bbde9c', '00bbdeaf']]`
  - `FALL_THROUGH` [`00bbdeac`](#insn-00bbdeac) → [`00bbdeb0`](#insn-00bbdeb0)
- ブロック [`00bbdeb0`](#insn-00bbdeb0) 範囲 `[['00bbdeb0', '00bbdeb3']]`
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe498`](#insn-00bbe498)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe88c`](#insn-00bbe88c)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe644`](#insn-00bbe644)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe928`](#insn-00bbe928)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe960`](#insn-00bbe960)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe670`](#insn-00bbe670)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbdeb4`](#insn-00bbdeb4)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe69c`](#insn-00bbe69c)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe9f4`](#insn-00bbe9f4)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbebc0`](#insn-00bbebc0)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbeb8c`](#insn-00bbeb8c)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe874`](#insn-00bbe874)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe22c`](#insn-00bbe22c)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbdf58`](#insn-00bbdf58)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbec6c`](#insn-00bbec6c)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe2a8`](#insn-00bbe2a8)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbecec`](#insn-00bbecec)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe398`](#insn-00bbe398)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbea1c`](#insn-00bbea1c)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe1bc`](#insn-00bbe1bc)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe418`](#insn-00bbe418)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe974`](#insn-00bbe974)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe5c4`](#insn-00bbe5c4)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbea8c`](#insn-00bbea8c)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe4d4`](#insn-00bbe4d4)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe14c`](#insn-00bbe14c)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe0cc`](#insn-00bbe0cc)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe544`](#insn-00bbe544)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe6e0`](#insn-00bbe6e0)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbeb0c`](#insn-00bbeb0c)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe760`](#insn-00bbe760)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbdfec`](#insn-00bbdfec)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe318`](#insn-00bbe318)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbebec`](#insn-00bbebec)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbdf6c`](#insn-00bbdf6c)
  - `COMPUTED_JUMP` [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe05c`](#insn-00bbe05c)
- ブロック [`00bbdeb4`](#insn-00bbdeb4) 範囲 `[['00bbdeb4', '00bbdec3']]`
  - `FALL_THROUGH` [`00bbdec0`](#insn-00bbdec0) → [`00bbdec4`](#insn-00bbdec4)
- ブロック [`00bbdec4`](#insn-00bbdec4) 範囲 `[['00bbdec4', '00bbdec7']]`
  - `CONDITIONAL_JUMP` [`00bbdec4`](#insn-00bbdec4) → [`00bbdee4`](#insn-00bbdee4)
  - `FALL_THROUGH` [`00bbdec4`](#insn-00bbdec4) → [`00bbdec8`](#insn-00bbdec8)
- ブロック [`00bbdec8`](#insn-00bbdec8) 範囲 `[['00bbdec8', '00bbdecf']]`
  - `FALL_THROUGH` [`00bbdecc`](#insn-00bbdecc) → [`00bbded0`](#insn-00bbded0)
- ブロック [`00bbded0`](#insn-00bbded0) 範囲 `[['00bbded0', '00bbdee3']]`
  - `FALL_THROUGH` [`00bbdee0`](#insn-00bbdee0) → [`00bbdee4`](#insn-00bbdee4)
- ブロック [`00bbdee4`](#insn-00bbdee4) 範囲 `[['00bbdee4', '00bbdeef']]`
  - `CONDITIONAL_JUMP` [`00bbdeec`](#insn-00bbdeec) → [`00bbdf04`](#insn-00bbdf04)
  - `FALL_THROUGH` [`00bbdeec`](#insn-00bbdeec) → [`00bbdef0`](#insn-00bbdef0)
- ブロック [`00bbdef0`](#insn-00bbdef0) 範囲 `[['00bbdef0', '00bbdf03']]`
  - `FALL_THROUGH` [`00bbdf00`](#insn-00bbdf00) → [`00bbdf04`](#insn-00bbdf04)
- ブロック [`00bbdf04`](#insn-00bbdf04) 範囲 `[['00bbdf04', '00bbdf0b']]`
  - `CONDITIONAL_JUMP` [`00bbdf08`](#insn-00bbdf08) → [`00bbdf58`](#insn-00bbdf58)
  - `FALL_THROUGH` [`00bbdf08`](#insn-00bbdf08) → [`00bbdf0c`](#insn-00bbdf0c)
- ブロック [`00bbdf0c`](#insn-00bbdf0c) 範囲 `[['00bbdf0c', '00bbdf17']]`
  - `CONDITIONAL_JUMP` [`00bbdf14`](#insn-00bbdf14) → [`00bbe960`](#insn-00bbe960)
  - `FALL_THROUGH` [`00bbdf14`](#insn-00bbdf14) → [`00bbdf18`](#insn-00bbdf18)
- ブロック [`00bbdf18`](#insn-00bbdf18) 範囲 `[['00bbdf18', '00bbdf1f']]`
  - `CONDITIONAL_JUMP` [`00bbdf1c`](#insn-00bbdf1c) → [`00bbdf58`](#insn-00bbdf58)
  - `FALL_THROUGH` [`00bbdf1c`](#insn-00bbdf1c) → [`00bbdf20`](#insn-00bbdf20)
- ブロック [`00bbdf20`](#insn-00bbdf20) 範囲 `[['00bbdf20', '00bbdf27']]`
  - `FALL_THROUGH` [`00bbdf24`](#insn-00bbdf24) → [`00bbdf28`](#insn-00bbdf28)
- ブロック [`00bbdf28`](#insn-00bbdf28) 範囲 `[['00bbdf28', '00bbdf2f']]`
  - `CONDITIONAL_JUMP` [`00bbdf2c`](#insn-00bbdf2c) → [`00bbdf58`](#insn-00bbdf58)
  - `FALL_THROUGH` [`00bbdf2c`](#insn-00bbdf2c) → [`00bbdf30`](#insn-00bbdf30)
- ブロック [`00bbdf30`](#insn-00bbdf30) 範囲 `[['00bbdf30', '00bbdf33']]`
  - `FALL_THROUGH` [`00bbdf30`](#insn-00bbdf30) → [`00bbdf34`](#insn-00bbdf34)
- ブロック [`00bbdf34`](#insn-00bbdf34) 範囲 `[['00bbdf34', '00bbdf3f']]`
  - `CONDITIONAL_JUMP` [`00bbdf3c`](#insn-00bbdf3c) → [`00bbdf58`](#insn-00bbdf58)
  - `FALL_THROUGH` [`00bbdf3c`](#insn-00bbdf3c) → [`00bbdf40`](#insn-00bbdf40)
- ブロック [`00bbdf40`](#insn-00bbdf40) 範囲 `[['00bbdf40', '00bbdf57']]`
  - `CONDITIONAL_JUMP` [`00bbdf54`](#insn-00bbdf54) → [`00bbe960`](#insn-00bbe960)
  - `FALL_THROUGH` [`00bbdf54`](#insn-00bbdf54) → [`00bbdf58`](#insn-00bbdf58)
- ブロック [`00bbdf58`](#insn-00bbdf58) 範囲 `[['00bbdf58', '00bbdf67']]`
  - `CONDITIONAL_JUMP` [`00bbdf64`](#insn-00bbdf64) → [`00bbe89c`](#insn-00bbe89c)
  - `FALL_THROUGH` [`00bbdf64`](#insn-00bbdf64) → [`00bbdf68`](#insn-00bbdf68)
- ブロック [`00bbdf68`](#insn-00bbdf68) 範囲 `[['00bbdf68', '00bbdf6b']]`
  - `UNCONDITIONAL_JUMP` [`00bbdf68`](#insn-00bbdf68) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbdf6c`](#insn-00bbdf6c) 範囲 `[['00bbdf6c', '00bbdf8b']]`
  - `CONDITIONAL_JUMP` [`00bbdf88`](#insn-00bbdf88) → [`00bbdfa8`](#insn-00bbdfa8)
  - `FALL_THROUGH` [`00bbdf88`](#insn-00bbdf88) → [`00bbdf8c`](#insn-00bbdf8c)
- ブロック [`00bbdf8c`](#insn-00bbdf8c) 範囲 `[['00bbdf8c', '00bbdf97']]`
  - `CONDITIONAL_JUMP` [`00bbdf94`](#insn-00bbdf94) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbdf94`](#insn-00bbdf94) → [`00bbdf98`](#insn-00bbdf98)
- ブロック [`00bbdf98`](#insn-00bbdf98) 範囲 `[['00bbdf98', '00bbdfa7']]`
  - `FALL_THROUGH` [`00bbdfa4`](#insn-00bbdfa4) → [`00bbdfa8`](#insn-00bbdfa8)
- ブロック [`00bbdfa8`](#insn-00bbdfa8) 範囲 `[['00bbdfa8', '00bbdfeb']]`
  - `UNCONDITIONAL_JUMP` [`00bbdfe8`](#insn-00bbdfe8) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbdfec`](#insn-00bbdfec) 範囲 `[['00bbdfec', '00bbdfef']]`
  - `FALL_THROUGH` [`00bbdfec`](#insn-00bbdfec) → [`00bbdff0`](#insn-00bbdff0)
- ブロック [`00bbdff0`](#insn-00bbdff0) 範囲 `[['00bbdff0', '00bbdff3']]`
  - `FALL_THROUGH` [`00bbdff0`](#insn-00bbdff0) → [`00bbdff4`](#insn-00bbdff4)
- ブロック [`00bbdff4`](#insn-00bbdff4) 範囲 `[['00bbdff4', '00bbdff7']]`
  - `FALL_THROUGH` [`00bbdff4`](#insn-00bbdff4) → [`00bbdff8`](#insn-00bbdff8)
- ブロック [`00bbdff8`](#insn-00bbdff8) 範囲 `[['00bbdff8', '00bbdffb']]`
  - `FALL_THROUGH` [`00bbdff8`](#insn-00bbdff8) → [`00bbdffc`](#insn-00bbdffc)
- ブロック [`00bbdffc`](#insn-00bbdffc) 範囲 `[['00bbdffc', '00bbe00b']]`
  - `CONDITIONAL_JUMP` [`00bbe008`](#insn-00bbe008) → [`00bbe028`](#insn-00bbe028)
  - `FALL_THROUGH` [`00bbe008`](#insn-00bbe008) → [`00bbe00c`](#insn-00bbe00c)
- ブロック [`00bbe00c`](#insn-00bbe00c) 範囲 `[['00bbe00c', '00bbe013']]`
  - `FALL_THROUGH` [`00bbe010`](#insn-00bbe010) → [`00bbe014`](#insn-00bbe014)
- ブロック [`00bbe014`](#insn-00bbe014) 範囲 `[['00bbe014', '00bbe017']]`
  - `CONDITIONAL_JUMP` [`00bbe014`](#insn-00bbe014) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe014`](#insn-00bbe014) → [`00bbe018`](#insn-00bbe018)
- ブロック [`00bbe018`](#insn-00bbe018) 範囲 `[['00bbe018', '00bbe027']]`
  - `FALL_THROUGH` [`00bbe024`](#insn-00bbe024) → [`00bbe028`](#insn-00bbe028)
- ブロック [`00bbe028`](#insn-00bbe028) 範囲 `[['00bbe028', '00bbe02b']]`
  - `FALL_THROUGH` [`00bbe028`](#insn-00bbe028) → [`00bbe02c`](#insn-00bbe02c)
- ブロック [`00bbe02c`](#insn-00bbe02c) 範囲 `[['00bbe02c', '00bbe02f']]`
  - `FALL_THROUGH` [`00bbe02c`](#insn-00bbe02c) → [`00bbe030`](#insn-00bbe030)
- ブロック [`00bbe030`](#insn-00bbe030) 範囲 `[['00bbe030', '00bbe047']]`
  - `FALL_THROUGH` [`00bbe044`](#insn-00bbe044) → [`00bbe048`](#insn-00bbe048)
- ブロック [`00bbe048`](#insn-00bbe048) 範囲 `[['00bbe048', '00bbe05b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe058`](#insn-00bbe058) → [`00bbed58`](#insn-00bbed58)
- ブロック [`00bbe05c`](#insn-00bbe05c) 範囲 `[['00bbe05c', '00bbe05f']]`
  - `FALL_THROUGH` [`00bbe05c`](#insn-00bbe05c) → [`00bbe060`](#insn-00bbe060)
- ブロック [`00bbe060`](#insn-00bbe060) 範囲 `[['00bbe060', '00bbe077']]`
  - `FALL_THROUGH` [`00bbe074`](#insn-00bbe074) → [`00bbe078`](#insn-00bbe078)
- ブロック [`00bbe078`](#insn-00bbe078) 範囲 `[['00bbe078', '00bbe07b']]`
  - `CONDITIONAL_JUMP` [`00bbe078`](#insn-00bbe078) → [`00bbe098`](#insn-00bbe098)
  - `FALL_THROUGH` [`00bbe078`](#insn-00bbe078) → [`00bbe07c`](#insn-00bbe07c)
- ブロック [`00bbe07c`](#insn-00bbe07c) 範囲 `[['00bbe07c', '00bbe087']]`
  - `CONDITIONAL_JUMP` [`00bbe084`](#insn-00bbe084) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe084`](#insn-00bbe084) → [`00bbe088`](#insn-00bbe088)
- ブロック [`00bbe088`](#insn-00bbe088) 範囲 `[['00bbe088', '00bbe08b']]`
  - `FALL_THROUGH` [`00bbe088`](#insn-00bbe088) → [`00bbe08c`](#insn-00bbe08c)
- ブロック [`00bbe08c`](#insn-00bbe08c) 範囲 `[['00bbe08c', '00bbe08f']]`
  - `FALL_THROUGH` [`00bbe08c`](#insn-00bbe08c) → [`00bbe090`](#insn-00bbe090)
- ブロック [`00bbe090`](#insn-00bbe090) 範囲 `[['00bbe090', '00bbe093']]`
  - `FALL_THROUGH` [`00bbe090`](#insn-00bbe090) → [`00bbe094`](#insn-00bbe094)
- ブロック [`00bbe094`](#insn-00bbe094) 範囲 `[['00bbe094', '00bbe097']]`
  - `FALL_THROUGH` [`00bbe094`](#insn-00bbe094) → [`00bbe098`](#insn-00bbe098)
- ブロック [`00bbe098`](#insn-00bbe098) 範囲 `[['00bbe098', '00bbe0ab']]`
  - `FALL_THROUGH` [`00bbe0a8`](#insn-00bbe0a8) → [`00bbe0ac`](#insn-00bbe0ac)
- ブロック [`00bbe0ac`](#insn-00bbe0ac) 範囲 `[['00bbe0ac', '00bbe0bf']]`
  - `FALL_THROUGH` [`00bbe0bc`](#insn-00bbe0bc) → [`00bbe0c0`](#insn-00bbe0c0)
- ブロック [`00bbe0c0`](#insn-00bbe0c0) 範囲 `[['00bbe0c0', '00bbe0c3']]`
  - `FALL_THROUGH` [`00bbe0c0`](#insn-00bbe0c0) → [`00bbe0c4`](#insn-00bbe0c4)
- ブロック [`00bbe0c4`](#insn-00bbe0c4) 範囲 `[['00bbe0c4', '00bbe0c7']]`
  - `FALL_THROUGH` [`00bbe0c4`](#insn-00bbe0c4) → [`00bbe0c8`](#insn-00bbe0c8)
- ブロック [`00bbe0c8`](#insn-00bbe0c8) 範囲 `[['00bbe0c8', '00bbe0cb']]`
  - `UNCONDITIONAL_JUMP` [`00bbe0c8`](#insn-00bbe0c8) → [`00bbe630`](#insn-00bbe630)
- ブロック [`00bbe0cc`](#insn-00bbe0cc) 範囲 `[['00bbe0cc', '00bbe0df']]`
  - `FALL_THROUGH` [`00bbe0dc`](#insn-00bbe0dc) → [`00bbe0e0`](#insn-00bbe0e0)
- ブロック [`00bbe0e0`](#insn-00bbe0e0) 範囲 `[['00bbe0e0', '00bbe0eb']]`
  - `CONDITIONAL_JUMP` [`00bbe0e8`](#insn-00bbe0e8) → [`00bbe108`](#insn-00bbe108)
  - `FALL_THROUGH` [`00bbe0e8`](#insn-00bbe0e8) → [`00bbe0ec`](#insn-00bbe0ec)
- ブロック [`00bbe0ec`](#insn-00bbe0ec) 範囲 `[['00bbe0ec', '00bbe0f3']]`
  - `FALL_THROUGH` [`00bbe0f0`](#insn-00bbe0f0) → [`00bbe0f4`](#insn-00bbe0f4)
- ブロック [`00bbe0f4`](#insn-00bbe0f4) 範囲 `[['00bbe0f4', '00bbe0f7']]`
  - `CONDITIONAL_JUMP` [`00bbe0f4`](#insn-00bbe0f4) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe0f4`](#insn-00bbe0f4) → [`00bbe0f8`](#insn-00bbe0f8)
- ブロック [`00bbe0f8`](#insn-00bbe0f8) 範囲 `[['00bbe0f8', '00bbe107']]`
  - `FALL_THROUGH` [`00bbe104`](#insn-00bbe104) → [`00bbe108`](#insn-00bbe108)
- ブロック [`00bbe108`](#insn-00bbe108) 範囲 `[['00bbe108', '00bbe10f']]`
  - `FALL_THROUGH` [`00bbe10c`](#insn-00bbe10c) → [`00bbe110`](#insn-00bbe110)
- ブロック [`00bbe110`](#insn-00bbe110) 範囲 `[['00bbe110', '00bbe123']]`
  - `FALL_THROUGH` [`00bbe120`](#insn-00bbe120) → [`00bbe124`](#insn-00bbe124)
- ブロック [`00bbe124`](#insn-00bbe124) 範囲 `[['00bbe124', '00bbe127']]`
  - `FALL_THROUGH` [`00bbe124`](#insn-00bbe124) → [`00bbe128`](#insn-00bbe128)
- ブロック [`00bbe128`](#insn-00bbe128) 範囲 `[['00bbe128', '00bbe13f']]`
  - `FALL_THROUGH` [`00bbe13c`](#insn-00bbe13c) → [`00bbe140`](#insn-00bbe140)
- ブロック [`00bbe140`](#insn-00bbe140) 範囲 `[['00bbe140', '00bbe14b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe148`](#insn-00bbe148) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbe14c`](#insn-00bbe14c) 範囲 `[['00bbe14c', '00bbe16b']]`
  - `CONDITIONAL_JUMP` [`00bbe168`](#insn-00bbe168) → [`00bbe188`](#insn-00bbe188)
  - `FALL_THROUGH` [`00bbe168`](#insn-00bbe168) → [`00bbe16c`](#insn-00bbe16c)
- ブロック [`00bbe16c`](#insn-00bbe16c) 範囲 `[['00bbe16c', '00bbe177']]`
  - `CONDITIONAL_JUMP` [`00bbe174`](#insn-00bbe174) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe174`](#insn-00bbe174) → [`00bbe178`](#insn-00bbe178)
- ブロック [`00bbe178`](#insn-00bbe178) 範囲 `[['00bbe178', '00bbe187']]`
  - `FALL_THROUGH` [`00bbe184`](#insn-00bbe184) → [`00bbe188`](#insn-00bbe188)
- ブロック [`00bbe188`](#insn-00bbe188) 範囲 `[['00bbe188', '00bbe18b']]`
  - `FALL_THROUGH` [`00bbe188`](#insn-00bbe188) → [`00bbe18c`](#insn-00bbe18c)
- ブロック [`00bbe18c`](#insn-00bbe18c) 範囲 `[['00bbe18c', '00bbe18f']]`
  - `FALL_THROUGH` [`00bbe18c`](#insn-00bbe18c) → [`00bbe190`](#insn-00bbe190)
- ブロック [`00bbe190`](#insn-00bbe190) 範囲 `[['00bbe190', '00bbe193']]`
  - `FALL_THROUGH` [`00bbe190`](#insn-00bbe190) → [`00bbe194`](#insn-00bbe194)
- ブロック [`00bbe194`](#insn-00bbe194) 範囲 `[['00bbe194', '00bbe197']]`
  - `FALL_THROUGH` [`00bbe194`](#insn-00bbe194) → [`00bbe198`](#insn-00bbe198)
- ブロック [`00bbe198`](#insn-00bbe198) 範囲 `[['00bbe198', '00bbe19b']]`
  - `FALL_THROUGH` [`00bbe198`](#insn-00bbe198) → [`00bbe19c`](#insn-00bbe19c)
- ブロック [`00bbe19c`](#insn-00bbe19c) 範囲 `[['00bbe19c', '00bbe19f']]`
  - `FALL_THROUGH` [`00bbe19c`](#insn-00bbe19c) → [`00bbe1a0`](#insn-00bbe1a0)
- ブロック [`00bbe1a0`](#insn-00bbe1a0) 範囲 `[['00bbe1a0', '00bbe1a3']]`
  - `FALL_THROUGH` [`00bbe1a0`](#insn-00bbe1a0) → [`00bbe1a4`](#insn-00bbe1a4)
- ブロック [`00bbe1a4`](#insn-00bbe1a4) 範囲 `[['00bbe1a4', '00bbe1a7']]`
  - `FALL_THROUGH` [`00bbe1a4`](#insn-00bbe1a4) → [`00bbe1a8`](#insn-00bbe1a8)
- ブロック [`00bbe1a8`](#insn-00bbe1a8) 範囲 `[['00bbe1a8', '00bbe1bb']]`
  - `UNCONDITIONAL_JUMP` [`00bbe1b8`](#insn-00bbe1b8) → [`00bbe9e0`](#insn-00bbe9e0)
- ブロック [`00bbe1bc`](#insn-00bbe1bc) 範囲 `[['00bbe1bc', '00bbe1cf']]`
  - `FALL_THROUGH` [`00bbe1cc`](#insn-00bbe1cc) → [`00bbe1d0`](#insn-00bbe1d0)
- ブロック [`00bbe1d0`](#insn-00bbe1d0) 範囲 `[['00bbe1d0', '00bbe1db']]`
  - `CONDITIONAL_JUMP` [`00bbe1d8`](#insn-00bbe1d8) → [`00bbe1f8`](#insn-00bbe1f8)
  - `FALL_THROUGH` [`00bbe1d8`](#insn-00bbe1d8) → [`00bbe1dc`](#insn-00bbe1dc)
- ブロック [`00bbe1dc`](#insn-00bbe1dc) 範囲 `[['00bbe1dc', '00bbe1e7']]`
  - `CONDITIONAL_JUMP` [`00bbe1e4`](#insn-00bbe1e4) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe1e4`](#insn-00bbe1e4) → [`00bbe1e8`](#insn-00bbe1e8)
- ブロック [`00bbe1e8`](#insn-00bbe1e8) 範囲 `[['00bbe1e8', '00bbe1f7']]`
  - `FALL_THROUGH` [`00bbe1f4`](#insn-00bbe1f4) → [`00bbe1f8`](#insn-00bbe1f8)
- ブロック [`00bbe1f8`](#insn-00bbe1f8) 範囲 `[['00bbe1f8', '00bbe217']]`
  - `FALL_THROUGH` [`00bbe214`](#insn-00bbe214) → [`00bbe218`](#insn-00bbe218)
- ブロック [`00bbe218`](#insn-00bbe218) 範囲 `[['00bbe218', '00bbe22b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe228`](#insn-00bbe228) → [`00bbe74c`](#insn-00bbe74c)
- ブロック [`00bbe22c`](#insn-00bbe22c) 範囲 `[['00bbe22c', '00bbe237']]`
  - `CONDITIONAL_JUMP` [`00bbe234`](#insn-00bbe234) → [`00bbe260`](#insn-00bbe260)
  - `FALL_THROUGH` [`00bbe234`](#insn-00bbe234) → [`00bbe238`](#insn-00bbe238)
- ブロック [`00bbe238`](#insn-00bbe238) 範囲 `[['00bbe238', '00bbe247']]`
  - `CONDITIONAL_JUMP` [`00bbe244`](#insn-00bbe244) → [`00bbe260`](#insn-00bbe260)
  - `FALL_THROUGH` [`00bbe244`](#insn-00bbe244) → [`00bbe248`](#insn-00bbe248)
- ブロック [`00bbe248`](#insn-00bbe248) 範囲 `[['00bbe248', '00bbe25f']]`
  - `CONDITIONAL_JUMP` [`00bbe25c`](#insn-00bbe25c) → [`00bbe88c`](#insn-00bbe88c)
  - `FALL_THROUGH` [`00bbe25c`](#insn-00bbe25c) → [`00bbe260`](#insn-00bbe260)
- ブロック [`00bbe260`](#insn-00bbe260) 範囲 `[['00bbe260', '00bbe26f']]`
  - `CONDITIONAL_JUMP` [`00bbe26c`](#insn-00bbe26c) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbe26c`](#insn-00bbe26c) → [`00bbe270`](#insn-00bbe270)
- ブロック [`00bbe270`](#insn-00bbe270) 範囲 `[['00bbe270', '00bbe277']]`
  - `CONDITIONAL_JUMP` [`00bbe274`](#insn-00bbe274) → [`00bbe89c`](#insn-00bbe89c)
  - `FALL_THROUGH` [`00bbe274`](#insn-00bbe274) → [`00bbe278`](#insn-00bbe278)
- ブロック [`00bbe278`](#insn-00bbe278) 範囲 `[['00bbe278', '00bbe283']]`
  - `CONDITIONAL_JUMP` [`00bbe280`](#insn-00bbe280) → [`00bbe89c`](#insn-00bbe89c)
  - `FALL_THROUGH` [`00bbe280`](#insn-00bbe280) → [`00bbe284`](#insn-00bbe284)
- ブロック [`00bbe284`](#insn-00bbe284) 範囲 `[['00bbe284', '00bbe28f']]`
  - `CONDITIONAL_JUMP` [`00bbe28c`](#insn-00bbe28c) → [`00bbe89c`](#insn-00bbe89c)
  - `FALL_THROUGH` [`00bbe28c`](#insn-00bbe28c) → [`00bbe290`](#insn-00bbe290)
- ブロック [`00bbe290`](#insn-00bbe290) 範囲 `[['00bbe290', '00bbe29f']]`
  - `FALL_THROUGH` [`00bbe29c`](#insn-00bbe29c) → [`00bbe2a0`](#insn-00bbe2a0)
- ブロック [`00bbe2a0`](#insn-00bbe2a0) 範囲 `[['00bbe2a0', '00bbe2a3']]`
  - `CONDITIONAL_JUMP` [`00bbe2a0`](#insn-00bbe2a0) → [`00bbedf4`](#insn-00bbedf4)
  - `FALL_THROUGH` [`00bbe2a0`](#insn-00bbe2a0) → [`00bbe2a4`](#insn-00bbe2a4)
- ブロック [`00bbe2a4`](#insn-00bbe2a4) 範囲 `[['00bbe2a4', '00bbe2a7']]`
  - `UNCONDITIONAL_JUMP` [`00bbe2a4`](#insn-00bbe2a4) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbe2a8`](#insn-00bbe2a8) 範囲 `[['00bbe2a8', '00bbe2ab']]`
  - `FALL_THROUGH` [`00bbe2a8`](#insn-00bbe2a8) → [`00bbe2ac`](#insn-00bbe2ac)
- ブロック [`00bbe2ac`](#insn-00bbe2ac) 範囲 `[['00bbe2ac', '00bbe2bb']]`
  - `FALL_THROUGH` [`00bbe2b8`](#insn-00bbe2b8) → [`00bbe2bc`](#insn-00bbe2bc)
- ブロック [`00bbe2bc`](#insn-00bbe2bc) 範囲 `[['00bbe2bc', '00bbe2c7']]`
  - `CONDITIONAL_JUMP` [`00bbe2c4`](#insn-00bbe2c4) → [`00bbe2e4`](#insn-00bbe2e4)
  - `FALL_THROUGH` [`00bbe2c4`](#insn-00bbe2c4) → [`00bbe2c8`](#insn-00bbe2c8)
- ブロック [`00bbe2c8`](#insn-00bbe2c8) 範囲 `[['00bbe2c8', '00bbe2d3']]`
  - `CONDITIONAL_JUMP` [`00bbe2d0`](#insn-00bbe2d0) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe2d0`](#insn-00bbe2d0) → [`00bbe2d4`](#insn-00bbe2d4)
- ブロック [`00bbe2d4`](#insn-00bbe2d4) 範囲 `[['00bbe2d4', '00bbe2e3']]`
  - `FALL_THROUGH` [`00bbe2e0`](#insn-00bbe2e0) → [`00bbe2e4`](#insn-00bbe2e4)
- ブロック [`00bbe2e4`](#insn-00bbe2e4) 範囲 `[['00bbe2e4', '00bbe317']]`
  - `UNCONDITIONAL_JUMP` [`00bbe314`](#insn-00bbe314) → [`00bbed58`](#insn-00bbed58)
- ブロック [`00bbe318`](#insn-00bbe318) 範囲 `[['00bbe318', '00bbe337']]`
  - `CONDITIONAL_JUMP` [`00bbe334`](#insn-00bbe334) → [`00bbe354`](#insn-00bbe354)
  - `FALL_THROUGH` [`00bbe334`](#insn-00bbe334) → [`00bbe338`](#insn-00bbe338)
- ブロック [`00bbe338`](#insn-00bbe338) 範囲 `[['00bbe338', '00bbe343']]`
  - `CONDITIONAL_JUMP` [`00bbe340`](#insn-00bbe340) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe340`](#insn-00bbe340) → [`00bbe344`](#insn-00bbe344)
- ブロック [`00bbe344`](#insn-00bbe344) 範囲 `[['00bbe344', '00bbe353']]`
  - `FALL_THROUGH` [`00bbe350`](#insn-00bbe350) → [`00bbe354`](#insn-00bbe354)
- ブロック [`00bbe354`](#insn-00bbe354) 範囲 `[['00bbe354', '00bbe367']]`
  - `FALL_THROUGH` [`00bbe364`](#insn-00bbe364) → [`00bbe368`](#insn-00bbe368)
- ブロック [`00bbe368`](#insn-00bbe368) 範囲 `[['00bbe368', '00bbe377']]`
  - `FALL_THROUGH` [`00bbe374`](#insn-00bbe374) → [`00bbe378`](#insn-00bbe378)
- ブロック [`00bbe378`](#insn-00bbe378) 範囲 `[['00bbe378', '00bbe397']]`
  - `UNCONDITIONAL_JUMP` [`00bbe394`](#insn-00bbe394) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbe398`](#insn-00bbe398) 範囲 `[['00bbe398', '00bbe3b7']]`
  - `CONDITIONAL_JUMP` [`00bbe3b4`](#insn-00bbe3b4) → [`00bbe3d4`](#insn-00bbe3d4)
  - `FALL_THROUGH` [`00bbe3b4`](#insn-00bbe3b4) → [`00bbe3b8`](#insn-00bbe3b8)
- ブロック [`00bbe3b8`](#insn-00bbe3b8) 範囲 `[['00bbe3b8', '00bbe3c3']]`
  - `CONDITIONAL_JUMP` [`00bbe3c0`](#insn-00bbe3c0) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe3c0`](#insn-00bbe3c0) → [`00bbe3c4`](#insn-00bbe3c4)
- ブロック [`00bbe3c4`](#insn-00bbe3c4) 範囲 `[['00bbe3c4', '00bbe3d3']]`
  - `FALL_THROUGH` [`00bbe3d0`](#insn-00bbe3d0) → [`00bbe3d4`](#insn-00bbe3d4)
- ブロック [`00bbe3d4`](#insn-00bbe3d4) 範囲 `[['00bbe3d4', '00bbe3eb']]`
  - `FALL_THROUGH` [`00bbe3e8`](#insn-00bbe3e8) → [`00bbe3ec`](#insn-00bbe3ec)
- ブロック [`00bbe3ec`](#insn-00bbe3ec) 範囲 `[['00bbe3ec', '00bbe3ef']]`
  - `FALL_THROUGH` [`00bbe3ec`](#insn-00bbe3ec) → [`00bbe3f0`](#insn-00bbe3f0)
- ブロック [`00bbe3f0`](#insn-00bbe3f0) 範囲 `[['00bbe3f0', '00bbe417']]`
  - `UNCONDITIONAL_JUMP` [`00bbe414`](#insn-00bbe414) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbe418`](#insn-00bbe418) 範囲 `[['00bbe418', '00bbe437']]`
  - `CONDITIONAL_JUMP` [`00bbe434`](#insn-00bbe434) → [`00bbe454`](#insn-00bbe454)
  - `FALL_THROUGH` [`00bbe434`](#insn-00bbe434) → [`00bbe438`](#insn-00bbe438)
- ブロック [`00bbe438`](#insn-00bbe438) 範囲 `[['00bbe438', '00bbe443']]`
  - `CONDITIONAL_JUMP` [`00bbe440`](#insn-00bbe440) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe440`](#insn-00bbe440) → [`00bbe444`](#insn-00bbe444)
- ブロック [`00bbe444`](#insn-00bbe444) 範囲 `[['00bbe444', '00bbe453']]`
  - `FALL_THROUGH` [`00bbe450`](#insn-00bbe450) → [`00bbe454`](#insn-00bbe454)
- ブロック [`00bbe454`](#insn-00bbe454) 範囲 `[['00bbe454', '00bbe467']]`
  - `FALL_THROUGH` [`00bbe464`](#insn-00bbe464) → [`00bbe468`](#insn-00bbe468)
- ブロック [`00bbe468`](#insn-00bbe468) 範囲 `[['00bbe468', '00bbe497']]`
  - `UNCONDITIONAL_JUMP` [`00bbe494`](#insn-00bbe494) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbe498`](#insn-00bbe498) 範囲 `[['00bbe498', '00bbe4a7']]`
  - `FALL_THROUGH` [`00bbe4a4`](#insn-00bbe4a4) → [`00bbe4a8`](#insn-00bbe4a8)
- ブロック [`00bbe4a8`](#insn-00bbe4a8) 範囲 `[['00bbe4a8', '00bbe4af']]`
  - `CONDITIONAL_JUMP` [`00bbe4ac`](#insn-00bbe4ac) → [`00bbee08`](#insn-00bbee08)
  - `FALL_THROUGH` [`00bbe4ac`](#insn-00bbe4ac) → [`00bbe4b0`](#insn-00bbe4b0)
- ブロック [`00bbe4b0`](#insn-00bbe4b0) 範囲 `[['00bbe4b0', '00bbe4b3']]`
  - `FALL_THROUGH` [`00bbe4b0`](#insn-00bbe4b0) → [`00bbe4b4`](#insn-00bbe4b4)
- ブロック [`00bbe4b4`](#insn-00bbe4b4) 範囲 `[['00bbe4b4', '00bbe4bf']]`
  - `CONDITIONAL_JUMP` [`00bbe4bc`](#insn-00bbe4bc) → [`00bbee38`](#insn-00bbee38)
  - `FALL_THROUGH` [`00bbe4bc`](#insn-00bbe4bc) → [`00bbe4c0`](#insn-00bbe4c0)
- ブロック [`00bbe4c0`](#insn-00bbe4c0) 範囲 `[['00bbe4c0', '00bbe4c3']]`
  - `FALL_THROUGH` [`00bbe4c0`](#insn-00bbe4c0) → [`00bbe4c4`](#insn-00bbe4c4)
- ブロック [`00bbe4c4`](#insn-00bbe4c4) 範囲 `[['00bbe4c4', '00bbe4cb']]`
  - `CONDITIONAL_JUMP` [`00bbe4c8`](#insn-00bbe4c8) → [`00bbee08`](#insn-00bbee08)
  - `FALL_THROUGH` [`00bbe4c8`](#insn-00bbe4c8) → [`00bbe4cc`](#insn-00bbe4cc)
- ブロック [`00bbe4cc`](#insn-00bbe4cc) 範囲 `[['00bbe4cc', '00bbe4d3']]`
  - `UNCONDITIONAL_JUMP` [`00bbe4d0`](#insn-00bbe4d0) → [`00bbee74`](#insn-00bbee74)
- ブロック [`00bbe4d4`](#insn-00bbe4d4) 範囲 `[['00bbe4d4', '00bbe4f3']]`
  - `CONDITIONAL_JUMP` [`00bbe4f0`](#insn-00bbe4f0) → [`00bbe510`](#insn-00bbe510)
  - `FALL_THROUGH` [`00bbe4f0`](#insn-00bbe4f0) → [`00bbe4f4`](#insn-00bbe4f4)
- ブロック [`00bbe4f4`](#insn-00bbe4f4) 範囲 `[['00bbe4f4', '00bbe4ff']]`
  - `CONDITIONAL_JUMP` [`00bbe4fc`](#insn-00bbe4fc) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe4fc`](#insn-00bbe4fc) → [`00bbe500`](#insn-00bbe500)
- ブロック [`00bbe500`](#insn-00bbe500) 範囲 `[['00bbe500', '00bbe50f']]`
  - `FALL_THROUGH` [`00bbe50c`](#insn-00bbe50c) → [`00bbe510`](#insn-00bbe510)
- ブロック [`00bbe510`](#insn-00bbe510) 範囲 `[['00bbe510', '00bbe543']]`
  - `UNCONDITIONAL_JUMP` [`00bbe540`](#insn-00bbe540) → [`00bbed58`](#insn-00bbed58)
- ブロック [`00bbe544`](#insn-00bbe544) 範囲 `[['00bbe544', '00bbe563']]`
  - `CONDITIONAL_JUMP` [`00bbe560`](#insn-00bbe560) → [`00bbe580`](#insn-00bbe580)
  - `FALL_THROUGH` [`00bbe560`](#insn-00bbe560) → [`00bbe564`](#insn-00bbe564)
- ブロック [`00bbe564`](#insn-00bbe564) 範囲 `[['00bbe564', '00bbe567']]`
  - `FALL_THROUGH` [`00bbe564`](#insn-00bbe564) → [`00bbe568`](#insn-00bbe568)
- ブロック [`00bbe568`](#insn-00bbe568) 範囲 `[['00bbe568', '00bbe56f']]`
  - `CONDITIONAL_JUMP` [`00bbe56c`](#insn-00bbe56c) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe56c`](#insn-00bbe56c) → [`00bbe570`](#insn-00bbe570)
- ブロック [`00bbe570`](#insn-00bbe570) 範囲 `[['00bbe570', '00bbe573']]`
  - `FALL_THROUGH` [`00bbe570`](#insn-00bbe570) → [`00bbe574`](#insn-00bbe574)
- ブロック [`00bbe574`](#insn-00bbe574) 範囲 `[['00bbe574', '00bbe57f']]`
  - `FALL_THROUGH` [`00bbe57c`](#insn-00bbe57c) → [`00bbe580`](#insn-00bbe580)
- ブロック [`00bbe580`](#insn-00bbe580) 範囲 `[['00bbe580', '00bbe597']]`
  - `FALL_THROUGH` [`00bbe594`](#insn-00bbe594) → [`00bbe598`](#insn-00bbe598)
- ブロック [`00bbe598`](#insn-00bbe598) 範囲 `[['00bbe598', '00bbe5c3']]`
  - `UNCONDITIONAL_JUMP` [`00bbe5c0`](#insn-00bbe5c0) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbe5c4`](#insn-00bbe5c4) 範囲 `[['00bbe5c4', '00bbe5d7']]`
  - `FALL_THROUGH` [`00bbe5d4`](#insn-00bbe5d4) → [`00bbe5d8`](#insn-00bbe5d8)
- ブロック [`00bbe5d8`](#insn-00bbe5d8) 範囲 `[['00bbe5d8', '00bbe5e3']]`
  - `CONDITIONAL_JUMP` [`00bbe5e0`](#insn-00bbe5e0) → [`00bbe600`](#insn-00bbe600)
  - `FALL_THROUGH` [`00bbe5e0`](#insn-00bbe5e0) → [`00bbe5e4`](#insn-00bbe5e4)
- ブロック [`00bbe5e4`](#insn-00bbe5e4) 範囲 `[['00bbe5e4', '00bbe5ef']]`
  - `CONDITIONAL_JUMP` [`00bbe5ec`](#insn-00bbe5ec) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe5ec`](#insn-00bbe5ec) → [`00bbe5f0`](#insn-00bbe5f0)
- ブロック [`00bbe5f0`](#insn-00bbe5f0) 範囲 `[['00bbe5f0', '00bbe5f3']]`
  - `FALL_THROUGH` [`00bbe5f0`](#insn-00bbe5f0) → [`00bbe5f4`](#insn-00bbe5f4)
- ブロック [`00bbe5f4`](#insn-00bbe5f4) 範囲 `[['00bbe5f4', '00bbe5ff']]`
  - `FALL_THROUGH` [`00bbe5fc`](#insn-00bbe5fc) → [`00bbe600`](#insn-00bbe600)
- ブロック [`00bbe600`](#insn-00bbe600) 範囲 `[['00bbe600', '00bbe62f']]`
  - `FALL_THROUGH` [`00bbe62c`](#insn-00bbe62c) → [`00bbe630`](#insn-00bbe630)
- ブロック [`00bbe630`](#insn-00bbe630) 範囲 `[['00bbe630', '00bbe643']]`
  - `UNCONDITIONAL_JUMP` [`00bbe640`](#insn-00bbe640) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbe644`](#insn-00bbe644) 範囲 `[['00bbe644', '00bbe65f']]`
  - `CONDITIONAL_JUMP` [`00bbe65c`](#insn-00bbe65c) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbe65c`](#insn-00bbe65c) → [`00bbe660`](#insn-00bbe660)
- ブロック [`00bbe660`](#insn-00bbe660) 範囲 `[['00bbe660', '00bbe66f']]`
  - `UNCONDITIONAL_JUMP` [`00bbe66c`](#insn-00bbe66c) → [`00bbe89c`](#insn-00bbe89c)
- ブロック [`00bbe670`](#insn-00bbe670) 範囲 `[['00bbe670', '00bbe67b']]`
  - `FALL_THROUGH` [`00bbe678`](#insn-00bbe678) → [`00bbe67c`](#insn-00bbe67c)
- ブロック [`00bbe67c`](#insn-00bbe67c) 範囲 `[['00bbe67c', '00bbe68b']]`
  - `CONDITIONAL_JUMP` [`00bbe688`](#insn-00bbe688) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbe688`](#insn-00bbe688) → [`00bbe68c`](#insn-00bbe68c)
- ブロック [`00bbe68c`](#insn-00bbe68c) 範囲 `[['00bbe68c', '00bbe69b']]`
  - `UNCONDITIONAL_JUMP` [`00bbe698`](#insn-00bbe698) → [`00bbe89c`](#insn-00bbe89c)
- ブロック [`00bbe69c`](#insn-00bbe69c) 範囲 `[['00bbe69c', '00bbe6af']]`
  - `FALL_THROUGH` [`00bbe6ac`](#insn-00bbe6ac) → [`00bbe6b0`](#insn-00bbe6b0)
- ブロック [`00bbe6b0`](#insn-00bbe6b0) 範囲 `[['00bbe6b0', '00bbe6b7']]`
  - `CONDITIONAL_JUMP` [`00bbe6b4`](#insn-00bbe6b4) → [`00bbe898`](#insn-00bbe898)
  - `FALL_THROUGH` [`00bbe6b4`](#insn-00bbe6b4) → [`00bbe6b8`](#insn-00bbe6b8)
- ブロック [`00bbe6b8`](#insn-00bbe6b8) 範囲 `[['00bbe6b8', '00bbe6bb']]`
  - `FALL_THROUGH` [`00bbe6b8`](#insn-00bbe6b8) → [`00bbe6bc`](#insn-00bbe6bc)
- ブロック [`00bbe6bc`](#insn-00bbe6bc) 範囲 `[['00bbe6bc', '00bbe6c7']]`
  - `CONDITIONAL_JUMP` [`00bbe6c4`](#insn-00bbe6c4) → [`00bbe898`](#insn-00bbe898)
  - `FALL_THROUGH` [`00bbe6c4`](#insn-00bbe6c4) → [`00bbe6c8`](#insn-00bbe6c8)
- ブロック [`00bbe6c8`](#insn-00bbe6c8) 範囲 `[['00bbe6c8', '00bbe6db']]`
  - `CONDITIONAL_JUMP` [`00bbe6d8`](#insn-00bbe6d8) → [`00bbe89c`](#insn-00bbe89c)
  - `FALL_THROUGH` [`00bbe6d8`](#insn-00bbe6d8) → [`00bbe6dc`](#insn-00bbe6dc)
- ブロック [`00bbe6dc`](#insn-00bbe6dc) 範囲 `[['00bbe6dc', '00bbe6df']]`
  - `UNCONDITIONAL_JUMP` [`00bbe6dc`](#insn-00bbe6dc) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbe6e0`](#insn-00bbe6e0) 範囲 `[['00bbe6e0', '00bbe6ef']]`
  - `FALL_THROUGH` [`00bbe6ec`](#insn-00bbe6ec) → [`00bbe6f0`](#insn-00bbe6f0)
- ブロック [`00bbe6f0`](#insn-00bbe6f0) 範囲 `[['00bbe6f0', '00bbe6fb']]`
  - `FALL_THROUGH` [`00bbe6f8`](#insn-00bbe6f8) → [`00bbe6fc`](#insn-00bbe6fc)
- ブロック [`00bbe6fc`](#insn-00bbe6fc) 範囲 `[['00bbe6fc', '00bbe6ff']]`
  - `CONDITIONAL_JUMP` [`00bbe6fc`](#insn-00bbe6fc) → [`00bbe71c`](#insn-00bbe71c)
  - `FALL_THROUGH` [`00bbe6fc`](#insn-00bbe6fc) → [`00bbe700`](#insn-00bbe700)
- ブロック [`00bbe700`](#insn-00bbe700) 範囲 `[['00bbe700', '00bbe70b']]`
  - `CONDITIONAL_JUMP` [`00bbe708`](#insn-00bbe708) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe708`](#insn-00bbe708) → [`00bbe70c`](#insn-00bbe70c)
- ブロック [`00bbe70c`](#insn-00bbe70c) 範囲 `[['00bbe70c', '00bbe71b']]`
  - `FALL_THROUGH` [`00bbe718`](#insn-00bbe718) → [`00bbe71c`](#insn-00bbe71c)
- ブロック [`00bbe71c`](#insn-00bbe71c) 範囲 `[['00bbe71c', '00bbe72f']]`
  - `FALL_THROUGH` [`00bbe72c`](#insn-00bbe72c) → [`00bbe730`](#insn-00bbe730)
- ブロック [`00bbe730`](#insn-00bbe730) 範囲 `[['00bbe730', '00bbe73b']]`
  - `FALL_THROUGH` [`00bbe738`](#insn-00bbe738) → [`00bbe73c`](#insn-00bbe73c)
- ブロック [`00bbe73c`](#insn-00bbe73c) 範囲 `[['00bbe73c', '00bbe74b']]`
  - `FALL_THROUGH` [`00bbe748`](#insn-00bbe748) → [`00bbe74c`](#insn-00bbe74c)
- ブロック [`00bbe74c`](#insn-00bbe74c) 範囲 `[['00bbe74c', '00bbe75f']]`
  - `UNCONDITIONAL_JUMP` [`00bbe75c`](#insn-00bbe75c) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbe760`](#insn-00bbe760) 範囲 `[['00bbe760', '00bbe76f']]`
  - `FALL_THROUGH` [`00bbe76c`](#insn-00bbe76c) → [`00bbe770`](#insn-00bbe770)
- ブロック [`00bbe770`](#insn-00bbe770) 範囲 `[['00bbe770', '00bbe773']]`
  - `CONDITIONAL_JUMP` [`00bbe770`](#insn-00bbe770) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbe770`](#insn-00bbe770) → [`00bbe774`](#insn-00bbe774)
- ブロック [`00bbe774`](#insn-00bbe774) 範囲 `[['00bbe774', '00bbe77b']]`
  - `FALL_THROUGH` [`00bbe778`](#insn-00bbe778) → [`00bbe77c`](#insn-00bbe77c)
- ブロック [`00bbe77c`](#insn-00bbe77c) 範囲 `[['00bbe77c', '00bbe783']]`
  - `CONDITIONAL_JUMP` [`00bbe780`](#insn-00bbe780) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbe780`](#insn-00bbe780) → [`00bbe784`](#insn-00bbe784)
- ブロック [`00bbe784`](#insn-00bbe784) 範囲 `[['00bbe784', '00bbe78f']]`
  - `FALL_THROUGH` [`00bbe78c`](#insn-00bbe78c) → [`00bbe790`](#insn-00bbe790)
- ブロック [`00bbe790`](#insn-00bbe790) 範囲 `[['00bbe790', '00bbe7af']]`
  - `FALL_THROUGH` [`00bbe7ac`](#insn-00bbe7ac) → [`00bbe7b0`](#insn-00bbe7b0)
- ブロック [`00bbe7b0`](#insn-00bbe7b0) 範囲 `[['00bbe7b0', '00bbe7bb']]`
  - `CONDITIONAL_JUMP` [`00bbe7b8`](#insn-00bbe7b8) → [`00bbe7d0`](#insn-00bbe7d0)
  - `FALL_THROUGH` [`00bbe7b8`](#insn-00bbe7b8) → [`00bbe7bc`](#insn-00bbe7bc)
- ブロック [`00bbe7bc`](#insn-00bbe7bc) 範囲 `[['00bbe7bc', '00bbe7cf']]`
  - `CONDITIONAL_JUMP` [`00bbe7cc`](#insn-00bbe7cc) → [`00bbe790`](#insn-00bbe790)
  - `FALL_THROUGH` [`00bbe7cc`](#insn-00bbe7cc) → [`00bbe7d0`](#insn-00bbe7d0)
- ブロック [`00bbe7d0`](#insn-00bbe7d0) 範囲 `[['00bbe7d0', '00bbe7df']]`
  - `CONDITIONAL_JUMP` [`00bbe7dc`](#insn-00bbe7dc) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbe7dc`](#insn-00bbe7dc) → [`00bbe7e0`](#insn-00bbe7e0)
- ブロック [`00bbe7e0`](#insn-00bbe7e0) 範囲 `[['00bbe7e0', '00bbe7ef']]`
  - `FALL_THROUGH` [`00bbe7ec`](#insn-00bbe7ec) → [`00bbe7f0`](#insn-00bbe7f0)
- ブロック [`00bbe7f0`](#insn-00bbe7f0) 範囲 `[['00bbe7f0', '00bbe803']]`
  - `CONDITIONAL_JUMP` [`00bbe800`](#insn-00bbe800) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbe800`](#insn-00bbe800) → [`00bbe804`](#insn-00bbe804)
- ブロック [`00bbe804`](#insn-00bbe804) 範囲 `[['00bbe804', '00bbe80b']]`
  - `CONDITIONAL_JUMP` [`00bbe808`](#insn-00bbe808) → [`00bbeeb8`](#insn-00bbeeb8)
  - `FALL_THROUGH` [`00bbe808`](#insn-00bbe808) → [`00bbe80c`](#insn-00bbe80c)
- ブロック [`00bbe80c`](#insn-00bbe80c) 範囲 `[['00bbe80c', '00bbe817']]`
  - `CONDITIONAL_JUMP` [`00bbe814`](#insn-00bbe814) → [`00bbeeb8`](#insn-00bbeeb8)
  - `FALL_THROUGH` [`00bbe814`](#insn-00bbe814) → [`00bbe818`](#insn-00bbe818)
- ブロック [`00bbe818`](#insn-00bbe818) 範囲 `[['00bbe818', '00bbe83f']]`
  - `CONDITIONAL_JUMP` [`00bbe83c`](#insn-00bbe83c) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbe83c`](#insn-00bbe83c) → [`00bbe840`](#insn-00bbe840)
- ブロック [`00bbe840`](#insn-00bbe840) 範囲 `[['00bbe840', '00bbe84b']]`
  - `CONDITIONAL_JUMP` [`00bbe848`](#insn-00bbe848) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbe848`](#insn-00bbe848) → [`00bbe84c`](#insn-00bbe84c)
- ブロック [`00bbe84c`](#insn-00bbe84c) 範囲 `[['00bbe84c', '00bbe857']]`
  - `CONDITIONAL_JUMP` [`00bbe854`](#insn-00bbe854) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbe854`](#insn-00bbe854) → [`00bbe858`](#insn-00bbe858)
- ブロック [`00bbe858`](#insn-00bbe858) 範囲 `[['00bbe858', '00bbe873']]`
  - `UNCONDITIONAL_JUMP` [`00bbe870`](#insn-00bbe870) → [`00bbe89c`](#insn-00bbe89c)
- ブロック [`00bbe874`](#insn-00bbe874) 範囲 `[['00bbe874', '00bbe87f']]`
  - `CONDITIONAL_JUMP` [`00bbe87c`](#insn-00bbe87c) → [`00bbed8c`](#insn-00bbed8c)
  - `FALL_THROUGH` [`00bbe87c`](#insn-00bbe87c) → [`00bbe880`](#insn-00bbe880)
- ブロック [`00bbe880`](#insn-00bbe880) 範囲 `[['00bbe880', '00bbe88b']]`
  - `CONDITIONAL_JUMP` [`00bbe888`](#insn-00bbe888) → [`00bbed8c`](#insn-00bbed8c)
  - `FALL_THROUGH` [`00bbe888`](#insn-00bbe888) → [`00bbe88c`](#insn-00bbe88c)
- ブロック [`00bbe88c`](#insn-00bbe88c) 範囲 `[['00bbe88c', '00bbe897']]`
  - `FALL_THROUGH` [`00bbe894`](#insn-00bbe894) → [`00bbe898`](#insn-00bbe898)
- ブロック [`00bbe898`](#insn-00bbe898) 範囲 `[['00bbe898', '00bbe89b']]`
  - `CONDITIONAL_JUMP` [`00bbe898`](#insn-00bbe898) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbe898`](#insn-00bbe898) → [`00bbe89c`](#insn-00bbe89c)
- ブロック [`00bbe89c`](#insn-00bbe89c) 範囲 `[['00bbe89c', '00bbe8a7']]`
  - `CONDITIONAL_JUMP` [`00bbe8a4`](#insn-00bbe8a4) → [`00bbe918`](#insn-00bbe918)
  - `FALL_THROUGH` [`00bbe8a4`](#insn-00bbe8a4) → [`00bbe8a8`](#insn-00bbe8a8)
- ブロック [`00bbe8a8`](#insn-00bbe8a8) 範囲 `[['00bbe8a8', '00bbe8af']]`
  - `FALL_THROUGH` [`00bbe8ac`](#insn-00bbe8ac) → [`00bbe8b0`](#insn-00bbe8b0)
- ブロック [`00bbe8b0`](#insn-00bbe8b0) 範囲 `[['00bbe8b0', '00bbe8c3']]`
  - `CONDITIONAL_JUMP` [`00bbe8c0`](#insn-00bbe8c0) → [`00bbe8d8`](#insn-00bbe8d8)
  - `FALL_THROUGH` [`00bbe8c0`](#insn-00bbe8c0) → [`00bbe8c4`](#insn-00bbe8c4)
- ブロック [`00bbe8c4`](#insn-00bbe8c4) 範囲 `[['00bbe8c4', '00bbe8d3']]`
  - `CONDITIONAL_JUMP` [`00bbe8d0`](#insn-00bbe8d0) → [`00bbe904`](#insn-00bbe904)
  - `FALL_THROUGH` [`00bbe8d0`](#insn-00bbe8d0) → [`00bbe8d4`](#insn-00bbe8d4)
- ブロック [`00bbe8d4`](#insn-00bbe8d4) 範囲 `[['00bbe8d4', '00bbe8d7']]`
- ブロック [`00bbe8d8`](#insn-00bbe8d8) 範囲 `[['00bbe8d8', '00bbe8e3']]`
  - `CONDITIONAL_JUMP` [`00bbe8e0`](#insn-00bbe8e0) → [`00bbf1f0`](#insn-00bbf1f0)
  - `FALL_THROUGH` [`00bbe8e0`](#insn-00bbe8e0) → [`00bbe8e4`](#insn-00bbe8e4)
- ブロック [`00bbe8e4`](#insn-00bbe8e4) 範囲 `[['00bbe8e4', '00bbe8eb']]`
  - `CONDITIONAL_JUMP` [`00bbe8e8`](#insn-00bbe8e8) → [`00bbe900`](#insn-00bbe900)
  - `FALL_THROUGH` [`00bbe8e8`](#insn-00bbe8e8) → [`00bbe8ec`](#insn-00bbe8ec)
- ブロック [`00bbe8ec`](#insn-00bbe8ec) 範囲 `[['00bbe8ec', '00bbe8f7']]`
  - `FALL_THROUGH` [`00bbe8f4`](#insn-00bbe8f4) → [`00bbe8f8`](#insn-00bbe8f8)
- ブロック [`00bbe8f8`](#insn-00bbe8f8) 範囲 `[['00bbe8f8', '00bbe8ff']]`
  - `FALL_THROUGH` [`00bbe8fc`](#insn-00bbe8fc) → [`00bbe900`](#insn-00bbe900)
- ブロック [`00bbe900`](#insn-00bbe900) 範囲 `[['00bbe900', '00bbe903']]`
  - `FALL_THROUGH` [`00bbe900`](#insn-00bbe900) → [`00bbe904`](#insn-00bbe904)
- ブロック [`00bbe904`](#insn-00bbe904) 範囲 `[['00bbe904', '00bbe917']]`
  - `FALL_THROUGH` [`00bbe914`](#insn-00bbe914) → [`00bbe918`](#insn-00bbe918)
- ブロック [`00bbe918`](#insn-00bbe918) 範囲 `[['00bbe918', '00bbe927']]`
  - `UNCONDITIONAL_JUMP` [`00bbe924`](#insn-00bbe924) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbe928`](#insn-00bbe928) 範囲 `[['00bbe928', '00bbe92f']]`
  - `FALL_THROUGH` [`00bbe92c`](#insn-00bbe92c) → [`00bbe930`](#insn-00bbe930)
- ブロック [`00bbe930`](#insn-00bbe930) 範囲 `[['00bbe930', '00bbe933']]`
  - `CONDITIONAL_JUMP` [`00bbe930`](#insn-00bbe930) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbe930`](#insn-00bbe930) → [`00bbe934`](#insn-00bbe934)
- ブロック [`00bbe934`](#insn-00bbe934) 範囲 `[['00bbe934', '00bbe947']]`
  - `CONDITIONAL_JUMP` [`00bbe944`](#insn-00bbe944) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbe944`](#insn-00bbe944) → [`00bbe948`](#insn-00bbe948)
- ブロック [`00bbe948`](#insn-00bbe948) 範囲 `[['00bbe948', '00bbe95b']]`
  - `FALL_THROUGH` [`00bbe958`](#insn-00bbe958) → [`00bbe95c`](#insn-00bbe95c)
- ブロック [`00bbe95c`](#insn-00bbe95c) 範囲 `[['00bbe95c', '00bbe95f']]`
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbef38`](#insn-00bbef38)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbed6c`](#insn-00bbed6c)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbf024`](#insn-00bbf024)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbeec8`](#insn-00bbeec8)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbe960`](#insn-00bbe960)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbef24`](#insn-00bbef24)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbf0e4`](#insn-00bbf0e4)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbf14c`](#insn-00bbf14c)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbf0b0`](#insn-00bbf0b0)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbeff0`](#insn-00bbeff0)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbf080`](#insn-00bbf080)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbf0a0`](#insn-00bbf0a0)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbf090`](#insn-00bbf090)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbf15c`](#insn-00bbf15c)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbefc4`](#insn-00bbefc4)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbf118`](#insn-00bbf118)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbef7c`](#insn-00bbef7c)
  - `COMPUTED_JUMP` [`00bbe95c`](#insn-00bbe95c) → [`00bbefb0`](#insn-00bbefb0)
- ブロック [`00bbe960`](#insn-00bbe960) 範囲 `[['00bbe960', '00bbe96f']]`
  - `CONDITIONAL_JUMP` [`00bbe96c`](#insn-00bbe96c) → [`00bbe89c`](#insn-00bbe89c)
  - `FALL_THROUGH` [`00bbe96c`](#insn-00bbe96c) → [`00bbe970`](#insn-00bbe970)
- ブロック [`00bbe970`](#insn-00bbe970) 範囲 `[['00bbe970', '00bbe973']]`
  - `UNCONDITIONAL_JUMP` [`00bbe970`](#insn-00bbe970) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbe974`](#insn-00bbe974) 範囲 `[['00bbe974', '00bbe993']]`
  - `CONDITIONAL_JUMP` [`00bbe990`](#insn-00bbe990) → [`00bbe9b0`](#insn-00bbe9b0)
  - `FALL_THROUGH` [`00bbe990`](#insn-00bbe990) → [`00bbe994`](#insn-00bbe994)
- ブロック [`00bbe994`](#insn-00bbe994) 範囲 `[['00bbe994', '00bbe997']]`
  - `FALL_THROUGH` [`00bbe994`](#insn-00bbe994) → [`00bbe998`](#insn-00bbe998)
- ブロック [`00bbe998`](#insn-00bbe998) 範囲 `[['00bbe998', '00bbe99f']]`
  - `CONDITIONAL_JUMP` [`00bbe99c`](#insn-00bbe99c) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbe99c`](#insn-00bbe99c) → [`00bbe9a0`](#insn-00bbe9a0)
- ブロック [`00bbe9a0`](#insn-00bbe9a0) 範囲 `[['00bbe9a0', '00bbe9af']]`
  - `FALL_THROUGH` [`00bbe9ac`](#insn-00bbe9ac) → [`00bbe9b0`](#insn-00bbe9b0)
- ブロック [`00bbe9b0`](#insn-00bbe9b0) 範囲 `[['00bbe9b0', '00bbe9df']]`
  - `FALL_THROUGH` [`00bbe9dc`](#insn-00bbe9dc) → [`00bbe9e0`](#insn-00bbe9e0)
- ブロック [`00bbe9e0`](#insn-00bbe9e0) 範囲 `[['00bbe9e0', '00bbe9f3']]`
  - `UNCONDITIONAL_JUMP` [`00bbe9f0`](#insn-00bbe9f0) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbe9f4`](#insn-00bbe9f4) 範囲 `[['00bbe9f4', '00bbea0f']]`
  - `CONDITIONAL_JUMP` [`00bbea0c`](#insn-00bbea0c) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbea0c`](#insn-00bbea0c) → [`00bbea10`](#insn-00bbea10)
- ブロック [`00bbea10`](#insn-00bbea10) 範囲 `[['00bbea10', '00bbea1b']]`
  - `UNCONDITIONAL_JUMP` [`00bbea18`](#insn-00bbea18) → [`00bbebac`](#insn-00bbebac)
- ブロック [`00bbea1c`](#insn-00bbea1c) 範囲 `[['00bbea1c', '00bbea3b']]`
  - `CONDITIONAL_JUMP` [`00bbea38`](#insn-00bbea38) → [`00bbea58`](#insn-00bbea58)
  - `FALL_THROUGH` [`00bbea38`](#insn-00bbea38) → [`00bbea3c`](#insn-00bbea3c)
- ブロック [`00bbea3c`](#insn-00bbea3c) 範囲 `[['00bbea3c', '00bbea47']]`
  - `CONDITIONAL_JUMP` [`00bbea44`](#insn-00bbea44) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbea44`](#insn-00bbea44) → [`00bbea48`](#insn-00bbea48)
- ブロック [`00bbea48`](#insn-00bbea48) 範囲 `[['00bbea48', '00bbea4f']]`
  - `FALL_THROUGH` [`00bbea4c`](#insn-00bbea4c) → [`00bbea50`](#insn-00bbea50)
- ブロック [`00bbea50`](#insn-00bbea50) 範囲 `[['00bbea50', '00bbea57']]`
  - `FALL_THROUGH` [`00bbea54`](#insn-00bbea54) → [`00bbea58`](#insn-00bbea58)
- ブロック [`00bbea58`](#insn-00bbea58) 範囲 `[['00bbea58', '00bbea8b']]`
  - `UNCONDITIONAL_JUMP` [`00bbea88`](#insn-00bbea88) → [`00bbecd8`](#insn-00bbecd8)
- ブロック [`00bbea8c`](#insn-00bbea8c) 範囲 `[['00bbea8c', '00bbeaab']]`
  - `CONDITIONAL_JUMP` [`00bbeaa8`](#insn-00bbeaa8) → [`00bbeac8`](#insn-00bbeac8)
  - `FALL_THROUGH` [`00bbeaa8`](#insn-00bbeaa8) → [`00bbeaac`](#insn-00bbeaac)
- ブロック [`00bbeaac`](#insn-00bbeaac) 範囲 `[['00bbeaac', '00bbeab3']]`
  - `FALL_THROUGH` [`00bbeab0`](#insn-00bbeab0) → [`00bbeab4`](#insn-00bbeab4)
- ブロック [`00bbeab4`](#insn-00bbeab4) 範囲 `[['00bbeab4', '00bbeab7']]`
  - `CONDITIONAL_JUMP` [`00bbeab4`](#insn-00bbeab4) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbeab4`](#insn-00bbeab4) → [`00bbeab8`](#insn-00bbeab8)
- ブロック [`00bbeab8`](#insn-00bbeab8) 範囲 `[['00bbeab8', '00bbeabb']]`
  - `FALL_THROUGH` [`00bbeab8`](#insn-00bbeab8) → [`00bbeabc`](#insn-00bbeabc)
- ブロック [`00bbeabc`](#insn-00bbeabc) 範囲 `[['00bbeabc', '00bbeac7']]`
  - `FALL_THROUGH` [`00bbeac4`](#insn-00bbeac4) → [`00bbeac8`](#insn-00bbeac8)
- ブロック [`00bbeac8`](#insn-00bbeac8) 範囲 `[['00bbeac8', '00bbeae3']]`
  - `FALL_THROUGH` [`00bbeae0`](#insn-00bbeae0) → [`00bbeae4`](#insn-00bbeae4)
- ブロック [`00bbeae4`](#insn-00bbeae4) 範囲 `[['00bbeae4', '00bbeb0b']]`
  - `UNCONDITIONAL_JUMP` [`00bbeb08`](#insn-00bbeb08) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbeb0c`](#insn-00bbeb0c) 範囲 `[['00bbeb0c', '00bbeb2b']]`
  - `CONDITIONAL_JUMP` [`00bbeb28`](#insn-00bbeb28) → [`00bbeb48`](#insn-00bbeb48)
  - `FALL_THROUGH` [`00bbeb28`](#insn-00bbeb28) → [`00bbeb2c`](#insn-00bbeb2c)
- ブロック [`00bbeb2c`](#insn-00bbeb2c) 範囲 `[['00bbeb2c', '00bbeb37']]`
  - `CONDITIONAL_JUMP` [`00bbeb34`](#insn-00bbeb34) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbeb34`](#insn-00bbeb34) → [`00bbeb38`](#insn-00bbeb38)
- ブロック [`00bbeb38`](#insn-00bbeb38) 範囲 `[['00bbeb38', '00bbeb47']]`
  - `FALL_THROUGH` [`00bbeb44`](#insn-00bbeb44) → [`00bbeb48`](#insn-00bbeb48)
- ブロック [`00bbeb48`](#insn-00bbeb48) 範囲 `[['00bbeb48', '00bbeb8b']]`
  - `UNCONDITIONAL_JUMP` [`00bbeb88`](#insn-00bbeb88) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbeb8c`](#insn-00bbeb8c) 範囲 `[['00bbeb8c', '00bbeba7']]`
  - `CONDITIONAL_JUMP` [`00bbeba4`](#insn-00bbeba4) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbeba4`](#insn-00bbeba4) → [`00bbeba8`](#insn-00bbeba8)
- ブロック [`00bbeba8`](#insn-00bbeba8) 範囲 `[['00bbeba8', '00bbebab']]`
  - `FALL_THROUGH` [`00bbeba8`](#insn-00bbeba8) → [`00bbebac`](#insn-00bbebac)
- ブロック [`00bbebac`](#insn-00bbebac) 範囲 `[['00bbebac', '00bbebbf']]`
  - `UNCONDITIONAL_JUMP` [`00bbebbc`](#insn-00bbebbc) → [`00bbe89c`](#insn-00bbe89c)
- ブロック [`00bbebc0`](#insn-00bbebc0) 範囲 `[['00bbebc0', '00bbebc7']]`
  - `FALL_THROUGH` [`00bbebc4`](#insn-00bbebc4) → [`00bbebc8`](#insn-00bbebc8)
- ブロック [`00bbebc8`](#insn-00bbebc8) 範囲 `[['00bbebc8', '00bbebcb']]`
  - `FALL_THROUGH` [`00bbebc8`](#insn-00bbebc8) → [`00bbebcc`](#insn-00bbebcc)
- ブロック [`00bbebcc`](#insn-00bbebcc) 範囲 `[['00bbebcc', '00bbebdb']]`
  - `CONDITIONAL_JUMP` [`00bbebd8`](#insn-00bbebd8) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbebd8`](#insn-00bbebd8) → [`00bbebdc`](#insn-00bbebdc)
- ブロック [`00bbebdc`](#insn-00bbebdc) 範囲 `[['00bbebdc', '00bbebeb']]`
  - `UNCONDITIONAL_JUMP` [`00bbebe8`](#insn-00bbebe8) → [`00bbe89c`](#insn-00bbe89c)
- ブロック [`00bbebec`](#insn-00bbebec) 範囲 `[['00bbebec', '00bbec0b']]`
  - `CONDITIONAL_JUMP` [`00bbec08`](#insn-00bbec08) → [`00bbec28`](#insn-00bbec28)
  - `FALL_THROUGH` [`00bbec08`](#insn-00bbec08) → [`00bbec0c`](#insn-00bbec0c)
- ブロック [`00bbec0c`](#insn-00bbec0c) 範囲 `[['00bbec0c', '00bbec17']]`
  - `CONDITIONAL_JUMP` [`00bbec14`](#insn-00bbec14) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbec14`](#insn-00bbec14) → [`00bbec18`](#insn-00bbec18)
- ブロック [`00bbec18`](#insn-00bbec18) 範囲 `[['00bbec18', '00bbec1b']]`
  - `FALL_THROUGH` [`00bbec18`](#insn-00bbec18) → [`00bbec1c`](#insn-00bbec1c)
- ブロック [`00bbec1c`](#insn-00bbec1c) 範囲 `[['00bbec1c', '00bbec27']]`
  - `FALL_THROUGH` [`00bbec24`](#insn-00bbec24) → [`00bbec28`](#insn-00bbec28)
- ブロック [`00bbec28`](#insn-00bbec28) 範囲 `[['00bbec28', '00bbec6b']]`
  - `UNCONDITIONAL_JUMP` [`00bbec68`](#insn-00bbec68) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbec6c`](#insn-00bbec6c) 範囲 `[['00bbec6c', '00bbec8b']]`
  - `CONDITIONAL_JUMP` [`00bbec88`](#insn-00bbec88) → [`00bbeca8`](#insn-00bbeca8)
  - `FALL_THROUGH` [`00bbec88`](#insn-00bbec88) → [`00bbec8c`](#insn-00bbec8c)
- ブロック [`00bbec8c`](#insn-00bbec8c) 範囲 `[['00bbec8c', '00bbec97']]`
  - `CONDITIONAL_JUMP` [`00bbec94`](#insn-00bbec94) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbec94`](#insn-00bbec94) → [`00bbec98`](#insn-00bbec98)
- ブロック [`00bbec98`](#insn-00bbec98) 範囲 `[['00bbec98', '00bbeca7']]`
  - `FALL_THROUGH` [`00bbeca4`](#insn-00bbeca4) → [`00bbeca8`](#insn-00bbeca8)
- ブロック [`00bbeca8`](#insn-00bbeca8) 範囲 `[['00bbeca8', '00bbecd7']]`
  - `FALL_THROUGH` [`00bbecd4`](#insn-00bbecd4) → [`00bbecd8`](#insn-00bbecd8)
- ブロック [`00bbecd8`](#insn-00bbecd8) 範囲 `[['00bbecd8', '00bbeceb']]`
  - `UNCONDITIONAL_JUMP` [`00bbece8`](#insn-00bbece8) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbecec`](#insn-00bbecec) 範囲 `[['00bbecec', '00bbed0b']]`
  - `CONDITIONAL_JUMP` [`00bbed08`](#insn-00bbed08) → [`00bbed28`](#insn-00bbed28)
  - `FALL_THROUGH` [`00bbed08`](#insn-00bbed08) → [`00bbed0c`](#insn-00bbed0c)
- ブロック [`00bbed0c`](#insn-00bbed0c) 範囲 `[['00bbed0c', '00bbed17']]`
  - `CONDITIONAL_JUMP` [`00bbed14`](#insn-00bbed14) → [`00bbf1ec`](#insn-00bbf1ec)
  - `FALL_THROUGH` [`00bbed14`](#insn-00bbed14) → [`00bbed18`](#insn-00bbed18)
- ブロック [`00bbed18`](#insn-00bbed18) 範囲 `[['00bbed18', '00bbed27']]`
  - `FALL_THROUGH` [`00bbed24`](#insn-00bbed24) → [`00bbed28`](#insn-00bbed28)
- ブロック [`00bbed28`](#insn-00bbed28) 範囲 `[['00bbed28', '00bbed57']]`
  - `FALL_THROUGH` [`00bbed54`](#insn-00bbed54) → [`00bbed58`](#insn-00bbed58)
- ブロック [`00bbed58`](#insn-00bbed58) 範囲 `[['00bbed58', '00bbed67']]`
  - `FALL_THROUGH` [`00bbed64`](#insn-00bbed64) → [`00bbed68`](#insn-00bbed68)
- ブロック [`00bbed68`](#insn-00bbed68) 範囲 `[['00bbed68', '00bbed6b']]`
  - `FALL_THROUGH` [`00bbed68`](#insn-00bbed68) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbed6c`](#insn-00bbed6c) 範囲 `[['00bbed6c', '00bbed77']]`
  - `FALL_THROUGH` [`00bbed74`](#insn-00bbed74) → [`00bbed78`](#insn-00bbed78)
- ブロック [`00bbed78`](#insn-00bbed78) 範囲 `[['00bbed78', '00bbed8b']]`
- ブロック [`00bbed8c`](#insn-00bbed8c) 範囲 `[['00bbed8c', '00bbeda7']]`
  - `CONDITIONAL_JUMP` [`00bbeda4`](#insn-00bbeda4) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbeda4`](#insn-00bbeda4) → [`00bbeda8`](#insn-00bbeda8)
- ブロック [`00bbeda8`](#insn-00bbeda8) 範囲 `[['00bbeda8', '00bbedab']]`
  - `FALL_THROUGH` [`00bbeda8`](#insn-00bbeda8) → [`00bbedac`](#insn-00bbedac)
- ブロック [`00bbedac`](#insn-00bbedac) 範囲 `[['00bbedac', '00bbedb3']]`
  - `CONDITIONAL_JUMP` [`00bbedb0`](#insn-00bbedb0) → [`00bbeeac`](#insn-00bbeeac)
  - `FALL_THROUGH` [`00bbedb0`](#insn-00bbedb0) → [`00bbedb4`](#insn-00bbedb4)
- ブロック [`00bbedb4`](#insn-00bbedb4) 範囲 `[['00bbedb4', '00bbedc3']]`
  - `CONDITIONAL_JUMP` [`00bbedc0`](#insn-00bbedc0) → [`00bbeeb0`](#insn-00bbeeb0)
  - `FALL_THROUGH` [`00bbedc0`](#insn-00bbedc0) → [`00bbedc4`](#insn-00bbedc4)
- ブロック [`00bbedc4`](#insn-00bbedc4) 範囲 `[['00bbedc4', '00bbedc7']]`
  - `CONDITIONAL_JUMP` [`00bbedc4`](#insn-00bbedc4) → [`00bbedd0`](#insn-00bbedd0)
  - `FALL_THROUGH` [`00bbedc4`](#insn-00bbedc4) → [`00bbedc8`](#insn-00bbedc8)
- ブロック [`00bbedc8`](#insn-00bbedc8) 範囲 `[['00bbedc8', '00bbedcf']]`
  - `CONDITIONAL_JUMP` [`00bbedcc`](#insn-00bbedcc) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbedcc`](#insn-00bbedcc) → [`00bbedd0`](#insn-00bbedd0)
- ブロック [`00bbedd0`](#insn-00bbedd0) 範囲 `[['00bbedd0', '00bbedd3']]`
  - `CONDITIONAL_JUMP` [`00bbedd0`](#insn-00bbedd0) → [`00bbede0`](#insn-00bbede0)
  - `FALL_THROUGH` [`00bbedd0`](#insn-00bbedd0) → [`00bbedd4`](#insn-00bbedd4)
- ブロック [`00bbedd4`](#insn-00bbedd4) 範囲 `[['00bbedd4', '00bbeddf']]`
  - `FALL_THROUGH` [`00bbeddc`](#insn-00bbeddc) → [`00bbede0`](#insn-00bbede0)
- ブロック [`00bbede0`](#insn-00bbede0) 範囲 `[['00bbede0', '00bbede3']]`
  - `FALL_THROUGH` [`00bbede0`](#insn-00bbede0) → [`00bbede4`](#insn-00bbede4)
- ブロック [`00bbede4`](#insn-00bbede4) 範囲 `[['00bbede4', '00bbedf3']]`
  - `CONDITIONAL_JUMP` [`00bbedf0`](#insn-00bbedf0) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbedf0`](#insn-00bbedf0) → [`00bbedf4`](#insn-00bbedf4)
- ブロック [`00bbedf4`](#insn-00bbedf4) 範囲 `[['00bbedf4', '00bbedfb']]`
  - `FALL_THROUGH` [`00bbedf8`](#insn-00bbedf8) → [`00bbedfc`](#insn-00bbedfc)
- ブロック [`00bbedfc`](#insn-00bbedfc) 範囲 `[['00bbedfc', '00bbee07']]`
  - `UNCONDITIONAL_JUMP` [`00bbee04`](#insn-00bbee04) → [`00bbe89c`](#insn-00bbe89c)
- ブロック [`00bbee08`](#insn-00bbee08) 範囲 `[['00bbee08', '00bbee13']]`
  - `CONDITIONAL_JUMP` [`00bbee10`](#insn-00bbee10) → [`00bbe898`](#insn-00bbe898)
  - `FALL_THROUGH` [`00bbee10`](#insn-00bbee10) → [`00bbee14`](#insn-00bbee14)
- ブロック [`00bbee14`](#insn-00bbee14) 範囲 `[['00bbee14', '00bbee1f']]`
  - `CONDITIONAL_JUMP` [`00bbee1c`](#insn-00bbee1c) → [`00bbeea0`](#insn-00bbeea0)
  - `FALL_THROUGH` [`00bbee1c`](#insn-00bbee1c) → [`00bbee20`](#insn-00bbee20)
- ブロック [`00bbee20`](#insn-00bbee20) 範囲 `[['00bbee20', '00bbee2b']]`
  - `CONDITIONAL_JUMP` [`00bbee28`](#insn-00bbee28) → [`00bbeea0`](#insn-00bbeea0)
  - `FALL_THROUGH` [`00bbee28`](#insn-00bbee28) → [`00bbee2c`](#insn-00bbee2c)
- ブロック [`00bbee2c`](#insn-00bbee2c) 範囲 `[['00bbee2c', '00bbee2f']]`
  - `FALL_THROUGH` [`00bbee2c`](#insn-00bbee2c) → [`00bbee30`](#insn-00bbee30)
- ブロック [`00bbee30`](#insn-00bbee30) 範囲 `[['00bbee30', '00bbee37']]`
  - `UNCONDITIONAL_JUMP` [`00bbee34`](#insn-00bbee34) → [`00bbee74`](#insn-00bbee74)
- ブロック [`00bbee38`](#insn-00bbee38) 範囲 `[['00bbee38', '00bbee4b']]`
  - `FALL_THROUGH` [`00bbee48`](#insn-00bbee48) → [`00bbee4c`](#insn-00bbee4c)
- ブロック [`00bbee4c`](#insn-00bbee4c) 範囲 `[['00bbee4c', '00bbee4f']]`
  - `FALL_THROUGH` [`00bbee4c`](#insn-00bbee4c) → [`00bbee50`](#insn-00bbee50)
- ブロック [`00bbee50`](#insn-00bbee50) 範囲 `[['00bbee50', '00bbee53']]`
  - `FALL_THROUGH` [`00bbee50`](#insn-00bbee50) → [`00bbee54`](#insn-00bbee54)
- ブロック [`00bbee54`](#insn-00bbee54) 範囲 `[['00bbee54', '00bbee63']]`
  - `CONDITIONAL_JUMP` [`00bbee60`](#insn-00bbee60) → [`00bbeea0`](#insn-00bbeea0)
  - `FALL_THROUGH` [`00bbee60`](#insn-00bbee60) → [`00bbee64`](#insn-00bbee64)
- ブロック [`00bbee64`](#insn-00bbee64) 範囲 `[['00bbee64', '00bbee6b']]`
  - `FALL_THROUGH` [`00bbee68`](#insn-00bbee68) → [`00bbee6c`](#insn-00bbee6c)
- ブロック [`00bbee6c`](#insn-00bbee6c) 範囲 `[['00bbee6c', '00bbee6f']]`
  - `CONDITIONAL_JUMP` [`00bbee6c`](#insn-00bbee6c) → [`00bbeea0`](#insn-00bbeea0)
  - `FALL_THROUGH` [`00bbee6c`](#insn-00bbee6c) → [`00bbee70`](#insn-00bbee70)
- ブロック [`00bbee70`](#insn-00bbee70) 範囲 `[['00bbee70', '00bbee73']]`
  - `FALL_THROUGH` [`00bbee70`](#insn-00bbee70) → [`00bbee74`](#insn-00bbee74)
- ブロック [`00bbee74`](#insn-00bbee74) 範囲 `[['00bbee74', '00bbee7f']]`
  - `FALL_THROUGH` [`00bbee7c`](#insn-00bbee7c) → [`00bbee80`](#insn-00bbee80)
- ブロック [`00bbee80`](#insn-00bbee80) 範囲 `[['00bbee80', '00bbee83']]`
  - `FALL_THROUGH` [`00bbee80`](#insn-00bbee80) → [`00bbee84`](#insn-00bbee84)
- ブロック [`00bbee84`](#insn-00bbee84) 範囲 `[['00bbee84', '00bbee87']]`
  - `CONDITIONAL_JUMP` [`00bbee84`](#insn-00bbee84) → [`00bbe898`](#insn-00bbe898)
  - `FALL_THROUGH` [`00bbee84`](#insn-00bbee84) → [`00bbee88`](#insn-00bbee88)
- ブロック [`00bbee88`](#insn-00bbee88) 範囲 `[['00bbee88', '00bbee9b']]`
  - `CONDITIONAL_JUMP` [`00bbee98`](#insn-00bbee98) → [`00bbe89c`](#insn-00bbe89c)
  - `FALL_THROUGH` [`00bbee98`](#insn-00bbee98) → [`00bbee9c`](#insn-00bbee9c)
- ブロック [`00bbee9c`](#insn-00bbee9c) 範囲 `[['00bbee9c', '00bbee9f']]`
  - `UNCONDITIONAL_JUMP` [`00bbee9c`](#insn-00bbee9c) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbeea0`](#insn-00bbeea0) 範囲 `[['00bbeea0', '00bbeea7']]`
  - `CONDITIONAL_JUMP` [`00bbeea4`](#insn-00bbeea4) → [`00bbe89c`](#insn-00bbe89c)
  - `FALL_THROUGH` [`00bbeea4`](#insn-00bbeea4) → [`00bbeea8`](#insn-00bbeea8)
- ブロック [`00bbeea8`](#insn-00bbeea8) 範囲 `[['00bbeea8', '00bbeeab']]`
  - `UNCONDITIONAL_JUMP` [`00bbeea8`](#insn-00bbeea8) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbeeac`](#insn-00bbeeac) 範囲 `[['00bbeeac', '00bbeeaf']]`
  - `FALL_THROUGH` [`00bbeeac`](#insn-00bbeeac) → [`00bbeeb0`](#insn-00bbeeb0)
- ブロック [`00bbeeb0`](#insn-00bbeeb0) 範囲 `[['00bbeeb0', '00bbeeb3']]`
  - `CONDITIONAL_JUMP` [`00bbeeb0`](#insn-00bbeeb0) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbeeb0`](#insn-00bbeeb0) → [`00bbeeb4`](#insn-00bbeeb4)
- ブロック [`00bbeeb4`](#insn-00bbeeb4) 範囲 `[['00bbeeb4', '00bbeeb7']]`
  - `UNCONDITIONAL_JUMP` [`00bbeeb4`](#insn-00bbeeb4) → [`00bbe89c`](#insn-00bbe89c)
- ブロック [`00bbeeb8`](#insn-00bbeeb8) 範囲 `[['00bbeeb8', '00bbeec7']]`
  - `UNCONDITIONAL_JUMP` [`00bbeec4`](#insn-00bbeec4) → [`00bbe89c`](#insn-00bbe89c)
- ブロック [`00bbeec8`](#insn-00bbeec8) 範囲 `[['00bbeec8', '00bbeecb']]`
  - `FALL_THROUGH` [`00bbeec8`](#insn-00bbeec8) → [`00bbeecc`](#insn-00bbeecc)
- ブロック [`00bbeecc`](#insn-00bbeecc) 範囲 `[['00bbeecc', '00bbeee3']]`
  - `FALL_THROUGH` [`00bbeee0`](#insn-00bbeee0) → [`00bbeee4`](#insn-00bbeee4)
- ブロック [`00bbeee4`](#insn-00bbeee4) 範囲 `[['00bbeee4', '00bbef07']]`
  - `FALL_THROUGH` [`00bbef04`](#insn-00bbef04) → [`00bbef08`](#insn-00bbef08)
- ブロック [`00bbef08`](#insn-00bbef08) 範囲 `[['00bbef08', '00bbef0f']]`
  - `CONDITIONAL_JUMP` [`00bbef0c`](#insn-00bbef0c) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbef0c`](#insn-00bbef0c) → [`00bbef10`](#insn-00bbef10)
- ブロック [`00bbef10`](#insn-00bbef10) 範囲 `[['00bbef10', '00bbef13']]`
  - `FALL_THROUGH` [`00bbef10`](#insn-00bbef10) → [`00bbef14`](#insn-00bbef14)
- ブロック [`00bbef14`](#insn-00bbef14) 範囲 `[['00bbef14', '00bbef23']]`
  - `UNCONDITIONAL_JUMP` [`00bbef20`](#insn-00bbef20) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbef24`](#insn-00bbef24) 範囲 `[['00bbef24', '00bbef2f']]`
  - `FALL_THROUGH` [`00bbef2c`](#insn-00bbef2c) → [`00bbef30`](#insn-00bbef30)
- ブロック [`00bbef30`](#insn-00bbef30) 範囲 `[['00bbef30', '00bbef33']]`
  - `CONDITIONAL_JUMP` [`00bbef30`](#insn-00bbef30) → [`00bbe89c`](#insn-00bbe89c)
  - `FALL_THROUGH` [`00bbef30`](#insn-00bbef30) → [`00bbef34`](#insn-00bbef34)
- ブロック [`00bbef34`](#insn-00bbef34) 範囲 `[['00bbef34', '00bbef37']]`
  - `UNCONDITIONAL_JUMP` [`00bbef34`](#insn-00bbef34) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbef38`](#insn-00bbef38) 範囲 `[['00bbef38', '00bbef3b']]`
  - `FALL_THROUGH` [`00bbef38`](#insn-00bbef38) → [`00bbef3c`](#insn-00bbef3c)
- ブロック [`00bbef3c`](#insn-00bbef3c) 範囲 `[['00bbef3c', '00bbef3f']]`
  - `FALL_THROUGH` [`00bbef3c`](#insn-00bbef3c) → [`00bbef40`](#insn-00bbef40)
- ブロック [`00bbef40`](#insn-00bbef40) 範囲 `[['00bbef40', '00bbef43']]`
  - `FALL_THROUGH` [`00bbef40`](#insn-00bbef40) → [`00bbef44`](#insn-00bbef44)
- ブロック [`00bbef44`](#insn-00bbef44) 範囲 `[['00bbef44', '00bbef47']]`
  - `FALL_THROUGH` [`00bbef44`](#insn-00bbef44) → [`00bbef48`](#insn-00bbef48)
- ブロック [`00bbef48`](#insn-00bbef48) 範囲 `[['00bbef48', '00bbef4b']]`
  - `FALL_THROUGH` [`00bbef48`](#insn-00bbef48) → [`00bbef4c`](#insn-00bbef4c)
- ブロック [`00bbef4c`](#insn-00bbef4c) 範囲 `[['00bbef4c', '00bbef4f']]`
  - `FALL_THROUGH` [`00bbef4c`](#insn-00bbef4c) → [`00bbef50`](#insn-00bbef50)
- ブロック [`00bbef50`](#insn-00bbef50) 範囲 `[['00bbef50', '00bbef57']]`
  - `CONDITIONAL_JUMP` [`00bbef54`](#insn-00bbef54) → [`00bbef68`](#insn-00bbef68)
  - `FALL_THROUGH` [`00bbef54`](#insn-00bbef54) → [`00bbef58`](#insn-00bbef58)
- ブロック [`00bbef58`](#insn-00bbef58) 範囲 `[['00bbef58', '00bbef63']]`
  - `FALL_THROUGH` [`00bbef60`](#insn-00bbef60) → [`00bbef64`](#insn-00bbef64)
- ブロック [`00bbef64`](#insn-00bbef64) 範囲 `[['00bbef64', '00bbef67']]`
  - `CONDITIONAL_JUMP` [`00bbef64`](#insn-00bbef64) → [`00bbf190`](#insn-00bbf190)
  - `FALL_THROUGH` [`00bbef64`](#insn-00bbef64) → [`00bbef68`](#insn-00bbef68)
- ブロック [`00bbef68`](#insn-00bbef68) 範囲 `[['00bbef68', '00bbef6b']]`
  - `FALL_THROUGH` [`00bbef68`](#insn-00bbef68) → [`00bbef6c`](#insn-00bbef6c)
- ブロック [`00bbef6c`](#insn-00bbef6c) 範囲 `[['00bbef6c', '00bbef6f']]`
  - `FALL_THROUGH` [`00bbef6c`](#insn-00bbef6c) → [`00bbef70`](#insn-00bbef70)
- ブロック [`00bbef70`](#insn-00bbef70) 範囲 `[['00bbef70', '00bbef73']]`
  - `FALL_THROUGH` [`00bbef70`](#insn-00bbef70) → [`00bbef74`](#insn-00bbef74)
- ブロック [`00bbef74`](#insn-00bbef74) 範囲 `[['00bbef74', '00bbef77']]`
  - `CONDITIONAL_JUMP` [`00bbef74`](#insn-00bbef74) → [`00bbf1b0`](#insn-00bbf1b0)
  - `FALL_THROUGH` [`00bbef74`](#insn-00bbef74) → [`00bbef78`](#insn-00bbef78)
- ブロック [`00bbef78`](#insn-00bbef78) 範囲 `[['00bbef78', '00bbef7b']]`
  - `UNCONDITIONAL_JUMP` [`00bbef78`](#insn-00bbef78) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbef7c`](#insn-00bbef7c) 範囲 `[['00bbef7c', '00bbef7f']]`
  - `FALL_THROUGH` [`00bbef7c`](#insn-00bbef7c) → [`00bbef80`](#insn-00bbef80)
- ブロック [`00bbef80`](#insn-00bbef80) 範囲 `[['00bbef80', '00bbef83']]`
  - `FALL_THROUGH` [`00bbef80`](#insn-00bbef80) → [`00bbef84`](#insn-00bbef84)
- ブロック [`00bbef84`](#insn-00bbef84) 範囲 `[['00bbef84', '00bbef87']]`
  - `FALL_THROUGH` [`00bbef84`](#insn-00bbef84) → [`00bbef88`](#insn-00bbef88)
- ブロック [`00bbef88`](#insn-00bbef88) 範囲 `[['00bbef88', '00bbefaf']]`
- ブロック [`00bbefb0`](#insn-00bbefb0) 範囲 `[['00bbefb0', '00bbefbf']]`
  - `CONDITIONAL_JUMP` [`00bbefbc`](#insn-00bbefbc) → [`00bbe89c`](#insn-00bbe89c)
  - `FALL_THROUGH` [`00bbefbc`](#insn-00bbefbc) → [`00bbefc0`](#insn-00bbefc0)
- ブロック [`00bbefc0`](#insn-00bbefc0) 範囲 `[['00bbefc0', '00bbefc3']]`
  - `UNCONDITIONAL_JUMP` [`00bbefc0`](#insn-00bbefc0) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbefc4`](#insn-00bbefc4) 範囲 `[['00bbefc4', '00bbefcb']]`
  - `FALL_THROUGH` [`00bbefc8`](#insn-00bbefc8) → [`00bbefcc`](#insn-00bbefcc)
- ブロック [`00bbefcc`](#insn-00bbefcc) 範囲 `[['00bbefcc', '00bbefdf']]`
  - `CONDITIONAL_JUMP` [`00bbefdc`](#insn-00bbefdc) → [`00bbed6c`](#insn-00bbed6c)
  - `FALL_THROUGH` [`00bbefdc`](#insn-00bbefdc) → [`00bbefe0`](#insn-00bbefe0)
- ブロック [`00bbefe0`](#insn-00bbefe0) 範囲 `[['00bbefe0', '00bbefef']]`
  - `UNCONDITIONAL_JUMP` [`00bbefec`](#insn-00bbefec) → [`00bbe89c`](#insn-00bbe89c)
- ブロック [`00bbeff0`](#insn-00bbeff0) 範囲 `[['00bbeff0', '00bbf023']]`
- ブロック [`00bbf024`](#insn-00bbf024) 範囲 `[['00bbf024', '00bbf027']]`
  - `FALL_THROUGH` [`00bbf024`](#insn-00bbf024) → [`00bbf028`](#insn-00bbf028)
- ブロック [`00bbf028`](#insn-00bbf028) 範囲 `[['00bbf028', '00bbf05b']]`
  - `CONDITIONAL_JUMP` [`00bbf058`](#insn-00bbf058) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbf058`](#insn-00bbf058) → [`00bbf05c`](#insn-00bbf05c)
- ブロック [`00bbf05c`](#insn-00bbf05c) 範囲 `[['00bbf05c', '00bbf067']]`
  - `CONDITIONAL_JUMP` [`00bbf064`](#insn-00bbf064) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbf064`](#insn-00bbf064) → [`00bbf068`](#insn-00bbf068)
- ブロック [`00bbf068`](#insn-00bbf068) 範囲 `[['00bbf068', '00bbf07f']]`
  - `UNCONDITIONAL_JUMP` [`00bbf07c`](#insn-00bbf07c) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbf080`](#insn-00bbf080) 範囲 `[['00bbf080', '00bbf08f']]`
  - `UNCONDITIONAL_JUMP` [`00bbf08c`](#insn-00bbf08c) → [`00bbf0bc`](#insn-00bbf0bc)
- ブロック [`00bbf090`](#insn-00bbf090) 範囲 `[['00bbf090', '00bbf09f']]`
  - `UNCONDITIONAL_JUMP` [`00bbf09c`](#insn-00bbf09c) → [`00bbf124`](#insn-00bbf124)
- ブロック [`00bbf0a0`](#insn-00bbf0a0) 範囲 `[['00bbf0a0', '00bbf0af']]`
  - `UNCONDITIONAL_JUMP` [`00bbf0ac`](#insn-00bbf0ac) → [`00bbf0f0`](#insn-00bbf0f0)
- ブロック [`00bbf0b0`](#insn-00bbf0b0) 範囲 `[['00bbf0b0', '00bbf0bb']]`
  - `FALL_THROUGH` [`00bbf0b8`](#insn-00bbf0b8) → [`00bbf0bc`](#insn-00bbf0bc)
- ブロック [`00bbf0bc`](#insn-00bbf0bc) 範囲 `[['00bbf0bc', '00bbf0bf']]`
  - `FALL_THROUGH` [`00bbf0bc`](#insn-00bbf0bc) → [`00bbf0c0`](#insn-00bbf0c0)
- ブロック [`00bbf0c0`](#insn-00bbf0c0) 範囲 `[['00bbf0c0', '00bbf0c3']]`
  - `FALL_THROUGH` [`00bbf0c0`](#insn-00bbf0c0) → [`00bbf0c4`](#insn-00bbf0c4)
- ブロック [`00bbf0c4`](#insn-00bbf0c4) 範囲 `[['00bbf0c4', '00bbf0db']]`
  - `FALL_THROUGH` [`00bbf0d8`](#insn-00bbf0d8) → [`00bbf0dc`](#insn-00bbf0dc)
- ブロック [`00bbf0dc`](#insn-00bbf0dc) 範囲 `[['00bbf0dc', '00bbf0df']]`
  - `FALL_THROUGH` [`00bbf0dc`](#insn-00bbf0dc) → [`00bbf0e0`](#insn-00bbf0e0)
- ブロック [`00bbf0e0`](#insn-00bbf0e0) 範囲 `[['00bbf0e0', '00bbf0e3']]`
- ブロック [`00bbf0e4`](#insn-00bbf0e4) 範囲 `[['00bbf0e4', '00bbf0ef']]`
  - `FALL_THROUGH` [`00bbf0ec`](#insn-00bbf0ec) → [`00bbf0f0`](#insn-00bbf0f0)
- ブロック [`00bbf0f0`](#insn-00bbf0f0) 範囲 `[['00bbf0f0', '00bbf117']]`
- ブロック [`00bbf118`](#insn-00bbf118) 範囲 `[['00bbf118', '00bbf11f']]`
  - `FALL_THROUGH` [`00bbf11c`](#insn-00bbf11c) → [`00bbf120`](#insn-00bbf120)
- ブロック [`00bbf120`](#insn-00bbf120) 範囲 `[['00bbf120', '00bbf123']]`
  - `FALL_THROUGH` [`00bbf120`](#insn-00bbf120) → [`00bbf124`](#insn-00bbf124)
- ブロック [`00bbf124`](#insn-00bbf124) 範囲 `[['00bbf124', '00bbf14b']]`
- ブロック [`00bbf14c`](#insn-00bbf14c) 範囲 `[['00bbf14c', '00bbf15b']]`
  - `UNCONDITIONAL_JUMP` [`00bbf158`](#insn-00bbf158) → [`00bbf168`](#insn-00bbf168)
- ブロック [`00bbf15c`](#insn-00bbf15c) 範囲 `[['00bbf15c', '00bbf167']]`
  - `FALL_THROUGH` [`00bbf164`](#insn-00bbf164) → [`00bbf168`](#insn-00bbf168)
- ブロック [`00bbf168`](#insn-00bbf168) 範囲 `[['00bbf168', '00bbf16b']]`
  - `FALL_THROUGH` [`00bbf168`](#insn-00bbf168) → [`00bbf16c`](#insn-00bbf16c)
- ブロック [`00bbf16c`](#insn-00bbf16c) 範囲 `[['00bbf16c', '00bbf18f']]`
- ブロック [`00bbf190`](#insn-00bbf190) 範囲 `[['00bbf190', '00bbf1af']]`
  - `FALL_THROUGH` [`00bbf1ac`](#insn-00bbf1ac) → [`00bbf1b0`](#insn-00bbf1b0)
- ブロック [`00bbf1b0`](#insn-00bbf1b0) 範囲 `[['00bbf1b0', '00bbf1bb']]`
  - `CONDITIONAL_JUMP` [`00bbf1b8`](#insn-00bbf1b8) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbf1b8`](#insn-00bbf1b8) → [`00bbf1bc`](#insn-00bbf1bc)
- ブロック [`00bbf1bc`](#insn-00bbf1bc) 範囲 `[['00bbf1bc', '00bbf1c3']]`
  - `FALL_THROUGH` [`00bbf1c0`](#insn-00bbf1c0) → [`00bbf1c4`](#insn-00bbf1c4)
- ブロック [`00bbf1c4`](#insn-00bbf1c4) 範囲 `[['00bbf1c4', '00bbf1c7']]`
  - `CONDITIONAL_JUMP` [`00bbf1c4`](#insn-00bbf1c4) → [`00bbf1e4`](#insn-00bbf1e4)
  - `FALL_THROUGH` [`00bbf1c4`](#insn-00bbf1c4) → [`00bbf1c8`](#insn-00bbf1c8)
- ブロック [`00bbf1c8`](#insn-00bbf1c8) 範囲 `[['00bbf1c8', '00bbf1e3']]`
  - `UNCONDITIONAL_JUMP` [`00bbf1e0`](#insn-00bbf1e0) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbf1e4`](#insn-00bbf1e4) 範囲 `[['00bbf1e4', '00bbf1eb']]`
  - `UNCONDITIONAL_JUMP` [`00bbf1e8`](#insn-00bbf1e8) → [`00bbed6c`](#insn-00bbed6c)
- ブロック [`00bbf1ec`](#insn-00bbf1ec) 範囲 `[['00bbf1ec', '00bbf1ef']]`
- ブロック [`00bbf1f0`](#insn-00bbf1f0) 範囲 `[['00bbf1f0', '00bbf1f3']]`

## 命令位置別の参照

- [`00bbde64`](#insn-00bbde64) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde68`](#insn-00bbde68) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde6c`](#insn-00bbde6c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde70`](#insn-00bbde70) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde80`](#insn-00bbde80) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbde88`](#insn-00bbde88) → [`00bbe88c`](#insn-00bbe88c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_42` · 推定型 `None`
- [`00bbde98`](#insn-00bbde98) → [`00bbe88c`](#insn-00bbe88c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_42` · 推定型 `None`
- [`00bbdea8`](#insn-00bbdea8) → `002fcb68`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::switchdataD_002fcb68` · 推定型 `ushort`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe498`](#insn-00bbe498) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_41` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe88c`](#insn-00bbe88c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_42` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe644`](#insn-00bbe644) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_43` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe928`](#insn-00bbe928) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_44` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe960`](#insn-00bbe960) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_46` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe670`](#insn-00bbe670) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_47` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbdeb4`](#insn-00bbdeb4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_4b` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe69c`](#insn-00bbe69c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_4d` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe9f4`](#insn-00bbe9f4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_4f` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbebc0`](#insn-00bbebc0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_50` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbeb8c`](#insn-00bbeb8c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_52` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe874`](#insn-00bbe874) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_53` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe22c`](#insn-00bbe22c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_54` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbdf58`](#insn-00bbdf58) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_55` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbec6c`](#insn-00bbec6c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_61` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe2a8`](#insn-00bbe2a8) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_62` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbecec`](#insn-00bbecec) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_63` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe398`](#insn-00bbe398) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_64` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbea1c`](#insn-00bbea1c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_65` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe1bc`](#insn-00bbe1bc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_66` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe418`](#insn-00bbe418) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_67` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe974`](#insn-00bbe974) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_68` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe5c4`](#insn-00bbe5c4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_69` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbea8c`](#insn-00bbea8c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_6a` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe4d4`](#insn-00bbe4d4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_6c` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe14c`](#insn-00bbe14c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_6d` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe0cc`](#insn-00bbe0cc) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_6e` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe544`](#insn-00bbe544) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_6f` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe6e0`](#insn-00bbe6e0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_73` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbeb0c`](#insn-00bbeb0c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_74` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe760`](#insn-00bbe760) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_75` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbdfec`](#insn-00bbdfec) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_76` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe318`](#insn-00bbe318) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_77` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbebec`](#insn-00bbebec) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_78` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbdf6c`](#insn-00bbdf6c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_79` · 推定型 `None`
- [`00bbdeb0`](#insn-00bbdeb0) → [`00bbe05c`](#insn-00bbe05c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_7a` · 推定型 `None`
- [`00bbdec4`](#insn-00bbdec4) → [`00bbdee4`](#insn-00bbdee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdeec`](#insn-00bbdeec) → [`00bbdf04`](#insn-00bbdf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf08`](#insn-00bbdf08) → [`00bbdf58`](#insn-00bbdf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_55` · 推定型 `None`
- [`00bbdf14`](#insn-00bbdf14) → [`00bbe960`](#insn-00bbe960) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_46` · 推定型 `None`
- [`00bbdf1c`](#insn-00bbdf1c) → [`00bbdf58`](#insn-00bbdf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_55` · 推定型 `None`
- [`00bbdf2c`](#insn-00bbdf2c) → [`00bbdf58`](#insn-00bbdf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_55` · 推定型 `None`
- [`00bbdf3c`](#insn-00bbdf3c) → [`00bbdf58`](#insn-00bbdf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_55` · 推定型 `None`
- [`00bbdf54`](#insn-00bbdf54) → [`00bbe960`](#insn-00bbe960) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_46` · 推定型 `None`
- [`00bbdf60`](#insn-00bbdf60) → [`00bd1778`](../00bd1/00bd1778.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd1778` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf64`](#insn-00bbdf64) → [`00bbe89c`](#insn-00bbe89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf68`](#insn-00bbdf68) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbdf88`](#insn-00bbdf88) → [`00bbdfa8`](#insn-00bbdfa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf90`](#insn-00bbdf90) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbdf94`](#insn-00bbdf94) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbdfc0`](#insn-00bbdfc0) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbdfe8`](#insn-00bbdfe8) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe008`](#insn-00bbe008) → [`00bbe028`](#insn-00bbe028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe010`](#insn-00bbe010) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe014`](#insn-00bbe014) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe040`](#insn-00bbe040) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe058`](#insn-00bbe058) → [`00bbed58`](#insn-00bbed58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe078`](#insn-00bbe078) → [`00bbe098`](#insn-00bbe098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe080`](#insn-00bbe080) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe084`](#insn-00bbe084) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0b0`](#insn-00bbe0b0) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe0c8`](#insn-00bbe0c8) → [`00bbe630`](#insn-00bbe630) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0e8`](#insn-00bbe0e8) → [`00bbe108`](#insn-00bbe108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0f0`](#insn-00bbe0f0) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe0f4`](#insn-00bbe0f4) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe120`](#insn-00bbe120) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe144`](#insn-00bbe144) → `0029365e`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbe148`](#insn-00bbe148) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbe168`](#insn-00bbe168) → [`00bbe188`](#insn-00bbe188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe170`](#insn-00bbe170) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe174`](#insn-00bbe174) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1a0`](#insn-00bbe1a0) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe1b8`](#insn-00bbe1b8) → [`00bbe9e0`](#insn-00bbe9e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1d8`](#insn-00bbe1d8) → [`00bbe1f8`](#insn-00bbe1f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1e0`](#insn-00bbe1e0) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe1e4`](#insn-00bbe1e4) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe210`](#insn-00bbe210) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe228`](#insn-00bbe228) → [`00bbe74c`](#insn-00bbe74c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe234`](#insn-00bbe234) → [`00bbe260`](#insn-00bbe260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe244`](#insn-00bbe244) → [`00bbe260`](#insn-00bbe260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe25c`](#insn-00bbe25c) → [`00bbe88c`](#insn-00bbe88c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_42` · 推定型 `None`
- [`00bbe264`](#insn-00bbe264) → [`00bc1ccc`](../00bc1/00bc1ccc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc1ccc` · 推定シンボル `None` · 推定型 `None`
- [`00bbe268`](#insn-00bbe268) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe26c`](#insn-00bbe26c) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbe274`](#insn-00bbe274) → [`00bbe89c`](#insn-00bbe89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe280`](#insn-00bbe280) → [`00bbe89c`](#insn-00bbe89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe28c`](#insn-00bbe28c) → [`00bbe89c`](#insn-00bbe89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe298`](#insn-00bbe298) → [`00bc1754`](../00bc1/00bc1754.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc1754` · 推定シンボル `None` · 推定型 `None`
- [`00bbe29c`](#insn-00bbe29c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2a0`](#insn-00bbe2a0) → [`00bbedf4`](#insn-00bbedf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2a4`](#insn-00bbe2a4) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbe2c4`](#insn-00bbe2c4) → [`00bbe2e4`](#insn-00bbe2e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2cc`](#insn-00bbe2cc) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2d0`](#insn-00bbe2d0) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe2fc`](#insn-00bbe2fc) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe314`](#insn-00bbe314) → [`00bbed58`](#insn-00bbed58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe334`](#insn-00bbe334) → [`00bbe354`](#insn-00bbe354) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe33c`](#insn-00bbe33c) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe340`](#insn-00bbe340) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe36c`](#insn-00bbe36c) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe394`](#insn-00bbe394) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3b4`](#insn-00bbe3b4) → [`00bbe3d4`](#insn-00bbe3d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3bc`](#insn-00bbe3bc) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3c0`](#insn-00bbe3c0) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe3ec`](#insn-00bbe3ec) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe414`](#insn-00bbe414) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe434`](#insn-00bbe434) → [`00bbe454`](#insn-00bbe454) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe43c`](#insn-00bbe43c) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe440`](#insn-00bbe440) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe46c`](#insn-00bbe46c) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe494`](#insn-00bbe494) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4a0`](#insn-00bbe4a0) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4ac`](#insn-00bbe4ac) → [`00bbee08`](#insn-00bbee08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4bc`](#insn-00bbe4bc) → [`00bbee38`](#insn-00bbee38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4c8`](#insn-00bbe4c8) → [`00bbee08`](#insn-00bbee08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4d0`](#insn-00bbe4d0) → [`00bbee74`](#insn-00bbee74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4f0`](#insn-00bbe4f0) → [`00bbe510`](#insn-00bbe510) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4f8`](#insn-00bbe4f8) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe4fc`](#insn-00bbe4fc) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe528`](#insn-00bbe528) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe540`](#insn-00bbe540) → [`00bbed58`](#insn-00bbed58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe560`](#insn-00bbe560) → [`00bbe580`](#insn-00bbe580) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe568`](#insn-00bbe568) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe56c`](#insn-00bbe56c) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe598`](#insn-00bbe598) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe5c0`](#insn-00bbe5c0) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5e0`](#insn-00bbe5e0) → [`00bbe600`](#insn-00bbe600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5e8`](#insn-00bbe5e8) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe5ec`](#insn-00bbe5ec) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe618`](#insn-00bbe618) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe640`](#insn-00bbe640) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe654`](#insn-00bbe654) → [`00bbde5c`](#insn-00bbde5c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bbe658`](#insn-00bbe658) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe65c`](#insn-00bbe65c) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbe668`](#insn-00bbe668) → [`00bd256c`](../00bd2/00bd256c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd256c` · 推定シンボル `None` · 推定型 `None`
- [`00bbe66c`](#insn-00bbe66c) → [`00bbe89c`](#insn-00bbe89c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe680`](#insn-00bbe680) → [`00bbde5c`](#insn-00bbde5c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bbe684`](#insn-00bbe684) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe688`](#insn-00bbe688) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbe694`](#insn-00bbe694) → [`00bd261c`](../00bd2/00bd261c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd261c` · 推定シンボル `None` · 推定型 `None`
- [`00bbe698`](#insn-00bbe698) → [`00bbe89c`](#insn-00bbe89c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6ac`](#insn-00bbe6ac) → [`00bbde5c`](#insn-00bbde5c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6b0`](#insn-00bbe6b0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6b4`](#insn-00bbe6b4) → [`00bbe898`](#insn-00bbe898) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6bc`](#insn-00bbe6bc) → [`00bbde5c`](#insn-00bbde5c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6c0`](#insn-00bbe6c0) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6c4`](#insn-00bbe6c4) → [`00bbe898`](#insn-00bbe898) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6d4`](#insn-00bbe6d4) → [`00bd4008`](../00bd4/00bd4008.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd4008` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6d8`](#insn-00bbe6d8) → [`00bbe89c`](#insn-00bbe89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe6dc`](#insn-00bbe6dc) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbe6fc`](#insn-00bbe6fc) → [`00bbe71c`](#insn-00bbe71c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe704`](#insn-00bbe704) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe708`](#insn-00bbe708) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe734`](#insn-00bbe734) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe75c`](#insn-00bbe75c) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe770`](#insn-00bbe770) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe780`](#insn-00bbe780) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7b8`](#insn-00bbe7b8) → [`00bbe7d0`](#insn-00bbe7d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7cc`](#insn-00bbe7cc) → [`00bbe790`](#insn-00bbe790) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7dc`](#insn-00bbe7dc) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe7e8`](#insn-00bbe7e8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe800`](#insn-00bbe800) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe808`](#insn-00bbe808) → [`00bbeeb8`](#insn-00bbeeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe814`](#insn-00bbe814) → [`00bbeeb8`](#insn-00bbeeb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe834`](#insn-00bbe834) → [`00bbde5c`](#insn-00bbde5c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bbe838`](#insn-00bbe838) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe83c`](#insn-00bbe83c) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe848`](#insn-00bbe848) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe854`](#insn-00bbe854) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe86c`](#insn-00bbe86c) → [`00bd1d54`](../00bd1/00bd1d54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd1d54` · 推定シンボル `None` · 推定型 `None`
- [`00bbe870`](#insn-00bbe870) → [`00bbe89c`](#insn-00bbe89c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe87c`](#insn-00bbe87c) → [`00bbed8c`](#insn-00bbed8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe888`](#insn-00bbe888) → [`00bbed8c`](#insn-00bbed8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe894`](#insn-00bbe894) → [`00bd22b4`](../00bd2/00bd22b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd22b4` · 推定シンボル `None` · 推定型 `None`
- [`00bbe898`](#insn-00bbe898) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbe8a4`](#insn-00bbe8a4) → [`00bbe918`](#insn-00bbe918) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8c0`](#insn-00bbe8c0) → [`00bbe8d8`](#insn-00bbe8d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8c8`](#insn-00bbe8c8) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8d0`](#insn-00bbe8d0) → [`00bbe904`](#insn-00bbe904) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8d4`](#insn-00bbe8d4) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8dc`](#insn-00bbe8dc) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8e0`](#insn-00bbe8e0) → [`00bbf1f0`](#insn-00bbf1f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8e8`](#insn-00bbe8e8) → [`00bbe900`](#insn-00bbe900) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe8f8`](#insn-00bbe8f8) → [`00bdb0f0`](../00bdb/00bdb0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe924`](#insn-00bbe924) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbe930`](#insn-00bbe930) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe944`](#insn-00bbe944) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbe954`](#insn-00bbe954) → `002fcbdc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::switchdataD_002fcbdc` · 推定型 `ushort`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbef38`](#insn-00bbef38) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_42` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbed6c`](#insn-00bbed6c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbf024`](#insn-00bbf024) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_46` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbeec8`](#insn-00bbeec8) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_4b` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbe960`](#insn-00bbe960) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbdeb0::caseD_46` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbef24`](#insn-00bbef24) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_54` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbf0e4`](#insn-00bbf0e4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_61` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbf14c`](#insn-00bbf14c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_63` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbf0b0`](#insn-00bbf0b0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_64` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbeff0`](#insn-00bbeff0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_65` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbf080`](#insn-00bbf080) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_66` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbf0a0`](#insn-00bbf0a0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_68` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbf090`](#insn-00bbf090) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_69` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbf15c`](#insn-00bbf15c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_6e` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbefc4`](#insn-00bbefc4) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_70` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbf118`](#insn-00bbf118) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_73` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbef7c`](#insn-00bbef7c) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_75` · 推定型 `None`
- [`00bbe95c`](#insn-00bbe95c) → [`00bbefb0`](#insn-00bbefb0) · `COMPUTED_JUMP` · `ANALYSIS` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_76` · 推定型 `None`
- [`00bbe968`](#insn-00bbe968) → [`00bd11d0`](../00bd1/00bd11d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd11d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe96c`](#insn-00bbe96c) → [`00bbe89c`](#insn-00bbe89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe970`](#insn-00bbe970) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbe990`](#insn-00bbe990) → [`00bbe9b0`](#insn-00bbe9b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe998`](#insn-00bbe998) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbe99c`](#insn-00bbe99c) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbe9c8`](#insn-00bbe9c8) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbe9f0`](#insn-00bbe9f0) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea04`](#insn-00bbea04) → [`00bbde5c`](#insn-00bbde5c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bbea08`](#insn-00bbea08) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea0c`](#insn-00bbea0c) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbea14`](#insn-00bbea14) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea18`](#insn-00bbea18) → [`00bbebac`](#insn-00bbebac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea38`](#insn-00bbea38) → [`00bbea58`](#insn-00bbea58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea40`](#insn-00bbea40) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbea44`](#insn-00bbea44) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbea70`](#insn-00bbea70) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbea88`](#insn-00bbea88) → [`00bbecd8`](#insn-00bbecd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeaa8`](#insn-00bbeaa8) → [`00bbeac8`](#insn-00bbeac8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeab0`](#insn-00bbeab0) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbeab4`](#insn-00bbeab4) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeae0`](#insn-00bbeae0) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbeb08`](#insn-00bbeb08) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb28`](#insn-00bbeb28) → [`00bbeb48`](#insn-00bbeb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb30`](#insn-00bbeb30) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb34`](#insn-00bbeb34) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb60`](#insn-00bbeb60) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbeb88`](#insn-00bbeb88) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeb9c`](#insn-00bbeb9c) → [`00bbde5c`](#insn-00bbde5c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bbeba0`](#insn-00bbeba0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeba4`](#insn-00bbeba4) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbeba8`](#insn-00bbeba8) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbebb8`](#insn-00bbebb8) → [`00bd24b0`](../00bd2/00bd24b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd24b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbebbc`](#insn-00bbebbc) → [`00bbe89c`](#insn-00bbe89c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbebd0`](#insn-00bbebd0) → [`00bbde5c`](#insn-00bbde5c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bbebd4`](#insn-00bbebd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbebd8`](#insn-00bbebd8) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbebe4`](#insn-00bbebe4) → [`00bd2404`](../00bd2/00bd2404.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd2404` · 推定シンボル `None` · 推定型 `None`
- [`00bbebe8`](#insn-00bbebe8) → [`00bbe89c`](#insn-00bbe89c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec08`](#insn-00bbec08) → [`00bbec28`](#insn-00bbec28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec10`](#insn-00bbec10) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbec14`](#insn-00bbec14) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec40`](#insn-00bbec40) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbec68`](#insn-00bbec68) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec88`](#insn-00bbec88) → [`00bbeca8`](#insn-00bbeca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbec90`](#insn-00bbec90) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbec94`](#insn-00bbec94) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbecc0`](#insn-00bbecc0) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbece8`](#insn-00bbece8) → [`00bbed68`](#insn-00bbed68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed08`](#insn-00bbed08) → [`00bbed28`](#insn-00bbed28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed10`](#insn-00bbed10) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbed14`](#insn-00bbed14) → [`00bbf1ec`](#insn-00bbf1ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed40`](#insn-00bbed40) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbed68`](#insn-00bbed68) → `0029aafb`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed68`](#insn-00bbed68) → `00290887`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbed68`](#insn-00bbed68) → `002a91d2`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbed68`](#insn-00bbed68) → `00290870`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbed68`](#insn-00bbed68) → `002ad7a7`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed68`](#insn-00bbed68) → `00290878`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbed68`](#insn-00bbed68) → `0029cf49`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbed68`](#insn-00bbed68) → `0029d2a2`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbed68`](#insn-00bbed68) → `002ad7ac`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbed68`](#insn-00bbed68) → `00291536`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed68`](#insn-00bbed68) → `002a730b`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbed68`](#insn-00bbed68) → `00291806`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbed68`](#insn-00bbed68) → `00297848`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbed68`](#insn-00bbed68) → `0029df19`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbed68`](#insn-00bbed68) → `002a125f`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed68`](#insn-00bbed68) → `002964e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed70`](#insn-00bbed70) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed74`](#insn-00bbed74) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed78`](#insn-00bbed78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed7c`](#insn-00bbed7c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed98`](#insn-00bbed98) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbed9c`](#insn-00bbed9c) → [`00bc15e4`](../00bc1/00bc15e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc15e4` · 推定シンボル `None` · 推定型 `None`
- [`00bbeda0`](#insn-00bbeda0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeda4`](#insn-00bbeda4) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedb0`](#insn-00bbedb0) → [`00bbeeac`](#insn-00bbeeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedb8`](#insn-00bbedb8) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedc0`](#insn-00bbedc0) → [`00bbeeb0`](#insn-00bbeeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedc4`](#insn-00bbedc4) → [`00bbedd0`](#insn-00bbedd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedcc`](#insn-00bbedcc) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbedd0`](#insn-00bbedd0) → [`00bbede0`](#insn-00bbede0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeddc`](#insn-00bbeddc) → [`00bbfdf8`](../00bbf/00bbfdf8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbfdf8` · 推定シンボル `None` · 推定型 `None`
- [`00bbede8`](#insn-00bbede8) → [`00bc1754`](../00bc1/00bc1754.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc1754` · 推定シンボル `None` · 推定型 `None`
- [`00bbedec`](#insn-00bbedec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbedf0`](#insn-00bbedf0) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee00`](#insn-00bbee00) → [`00bc1c24`](../00bc1/00bc1c24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc1c24` · 推定シンボル `None` · 推定型 `None`
- [`00bbee04`](#insn-00bbee04) → [`00bbe89c`](#insn-00bbe89c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee0c`](#insn-00bbee0c) → [`00bc2f0c`](../00bc2/00bc2f0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2f0c` · 推定シンボル `None` · 推定型 `None`
- [`00bbee10`](#insn-00bbee10) → [`00bbe898`](#insn-00bbe898) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee1c`](#insn-00bbee1c) → [`00bbeea0`](#insn-00bbeea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee28`](#insn-00bbee28) → [`00bbeea0`](#insn-00bbeea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee30`](#insn-00bbee30) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee34`](#insn-00bbee34) → [`00bbee74`](#insn-00bbee74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee40`](#insn-00bbee40) → [`00bbdd1c`](00bbdd1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd1c` · 推定シンボル `None` · 推定型 `None`
- [`00bbee44`](#insn-00bbee44) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee50`](#insn-00bbee50) → [`00bc2a60`](../00bc2/00bc2a60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2a60` · 推定シンボル `None` · 推定型 `None`
- [`00bbee58`](#insn-00bbee58) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee60`](#insn-00bbee60) → [`00bbeea0`](#insn-00bbeea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee6c`](#insn-00bbee6c) → [`00bbeea0`](#insn-00bbeea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee7c`](#insn-00bbee7c) → [`00bbde5c`](#insn-00bbde5c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bbee80`](#insn-00bbee80) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee84`](#insn-00bbee84) → [`00bbe898`](#insn-00bbe898) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee94`](#insn-00bbee94) → [`00bd3d8c`](../00bd3/00bd3d8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd3d8c` · 推定シンボル `None` · 推定型 `None`
- [`00bbee98`](#insn-00bbee98) → [`00bbe89c`](#insn-00bbe89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbee9c`](#insn-00bbee9c) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbeea4`](#insn-00bbeea4) → [`00bbe89c`](#insn-00bbe89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeea8`](#insn-00bbeea8) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbeeac`](#insn-00bbeeac) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeeb0`](#insn-00bbeeb0) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbeeb4`](#insn-00bbeeb4) → [`00bbe89c`](#insn-00bbe89c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeec0`](#insn-00bbeec0) → [`00bc136c`](../00bc1/00bc136c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc136c` · 推定シンボル `None` · 推定型 `None`
- [`00bbeec4`](#insn-00bbeec4) → [`00bbe89c`](#insn-00bbe89c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeefc`](#insn-00bbeefc) → `0029089a`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbeefc`](#insn-00bbeefc) → `002ac5ff`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbeefc`](#insn-00bbeefc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef04`](#insn-00bbef04) → [`00bbf39c`](../00bbf/00bbf39c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbf39c` · 推定シンボル `None` · 推定型 `None`
- [`00bbef08`](#insn-00bbef08) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef0c`](#insn-00bbef0c) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbef1c`](#insn-00bbef1c) → [`00bd1f4c`](../00bd1/00bd1f4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd1f4c` · 推定シンボル `None` · 推定型 `None`
- [`00bbef20`](#insn-00bbef20) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbef2c`](#insn-00bbef2c) → [`00bc2090`](../00bc2/00bc2090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2090` · 推定シンボル `None` · 推定型 `None`
- [`00bbef30`](#insn-00bbef30) → [`00bbe89c`](#insn-00bbe89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef34`](#insn-00bbef34) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbef50`](#insn-00bbef50) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef54`](#insn-00bbef54) → [`00bbef68`](#insn-00bbef68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef64`](#insn-00bbef64) → [`00bbf190`](#insn-00bbf190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef6c`](#insn-00bbef6c) → [`00bc2f0c`](../00bc2/00bc2f0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2f0c` · 推定シンボル `None` · 推定型 `None`
- [`00bbef70`](#insn-00bbef70) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef74`](#insn-00bbef74) → [`00bbf1b0`](#insn-00bbf1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef78`](#insn-00bbef78) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbef88`](#insn-00bbef88) → `00295789`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbef94`](#insn-00bbef94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef98`](#insn-00bbef98) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbef9c`](#insn-00bbef9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefa0`](#insn-00bbefa0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefac`](#insn-00bbefac) → [`00bc9604`](../00bc9/00bc9604.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc9604` · 推定シンボル `None` · 推定型 `None`
- [`00bbefb8`](#insn-00bbefb8) → [`00bd1ff8`](../00bd1/00bd1ff8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd1ff8` · 推定シンボル `None` · 推定型 `None`
- [`00bbefbc`](#insn-00bbefbc) → [`00bbe89c`](#insn-00bbe89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefc0`](#insn-00bbefc0) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbefd4`](#insn-00bbefd4) → [`00bbde5c`](#insn-00bbde5c) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bbefd8`](#insn-00bbefd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbefdc`](#insn-00bbefdc) → [`00bbed6c`](#insn-00bbed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbefe8`](#insn-00bbefe8) → [`00bc6374`](../00bc6/00bc6374.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc6374` · 推定シンボル `None` · 推定型 `None`
- [`00bbefec`](#insn-00bbefec) → [`00bbe89c`](#insn-00bbe89c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbeffc`](#insn-00bbeffc) → `0029aaff`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbf008`](#insn-00bbf008) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf00c`](#insn-00bbf00c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf010`](#insn-00bbf010) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf014`](#insn-00bbf014) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf020`](#insn-00bbf020) → [`00bd1ca8`](../00bd1/00bd1ca8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd1ca8` · 推定シンボル `None` · 推定型 `None`
- [`00bbf038`](#insn-00bbf038) → [`00bbdd1c`](00bbdd1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd1c` · 推定シンボル `None` · 推定型 `None`
- [`00bbf03c`](#insn-00bbf03c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf048`](#insn-00bbf048) → [`00bc2a60`](../00bc2/00bc2a60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2a60` · 推定シンボル `None` · 推定型 `None`
- [`00bbf050`](#insn-00bbf050) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf058`](#insn-00bbf058) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf064`](#insn-00bbf064) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf078`](#insn-00bbf078) → [`00bd1e00`](../00bd1/00bd1e00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd1e00` · 推定シンボル `None` · 推定型 `None`
- [`00bbf07c`](#insn-00bbf07c) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbf088`](#insn-00bbf088) → `002a535f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbf08c`](#insn-00bbf08c) → [`00bbf0bc`](#insn-00bbf0bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf098`](#insn-00bbf098) → `002a127d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbf09c`](#insn-00bbf09c) → [`00bbf124`](#insn-00bbf124) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0a8`](#insn-00bbf0a8) → `002a91e6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0ac`](#insn-00bbf0ac) → [`00bbf0f0`](#insn-00bbf0f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0b8`](#insn-00bbf0b8) → `002a91dc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbf0c8`](#insn-00bbf0c8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0cc`](#insn-00bbf0cc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0d0`](#insn-00bbf0d0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0d4`](#insn-00bbf0d4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0e0`](#insn-00bbf0e0) → [`00bd1b50`](../00bd1/00bd1b50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd1b50` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0ec`](#insn-00bbf0ec) → `002925bc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf0fc`](#insn-00bbf0fc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf100`](#insn-00bbf100) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf104`](#insn-00bbf104) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf108`](#insn-00bbf108) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf114`](#insn-00bbf114) → [`00bc2bd8`](../00bc2/00bc2bd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2bd8` · 推定シンボル `None` · 推定型 `None`
- [`00bbf120`](#insn-00bbf120) → `002af7fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbf130`](#insn-00bbf130) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf134`](#insn-00bbf134) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf138`](#insn-00bbf138) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf13c`](#insn-00bbf13c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf148`](#insn-00bbf148) → [`00bd1bfc`](../00bd1/00bd1bfc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd1bfc` · 推定シンボル `None` · 推定型 `None`
- [`00bbf154`](#insn-00bbf154) → `00291811`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbf158`](#insn-00bbf158) → [`00bbf168`](#insn-00bbf168) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf164`](#insn-00bbf164) → `00295791`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbf174`](#insn-00bbf174) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf178`](#insn-00bbf178) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf17c`](#insn-00bbf17c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf180`](#insn-00bbf180) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf18c`](#insn-00bbf18c) → [`00bd0280`](../00bd0/00bd0280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd0280` · 推定シンボル `None` · 推定型 `None`
- [`00bbf198`](#insn-00bbf198) → [`00bbdd1c`](00bbdd1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd1c` · 推定シンボル `None` · 推定型 `None`
- [`00bbf19c`](#insn-00bbf19c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1a8`](#insn-00bbf1a8) → [`00bc2a60`](../00bc2/00bc2a60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2a60` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1ac`](#insn-00bbf1ac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1b8`](#insn-00bbf1b8) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1c4`](#insn-00bbf1c4) → [`00bbf1e4`](#insn-00bbf1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1dc`](#insn-00bbf1dc) → [`00bd1ea0`](../00bd1/00bd1ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd1ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1e0`](#insn-00bbf1e0) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbf1e8`](#insn-00bbf1e8) → [`00bbed6c`](#insn-00bbed6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `switchD_00bbe95c::caseD_43` · 推定型 `None`
- [`00bbf1ec`](#insn-00bbf1ec) → [`00bdb1d0`](../00bdb/00bdb1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbf1f0`](#insn-00bbf1f0) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbde64`](#insn-00bbde64)

~~~json
{
  "source": "00bbde64",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde68`](#insn-00bbde68)

~~~json
{
  "source": "00bbde68",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde6c`](#insn-00bbde6c)

~~~json
{
  "source": "00bbde6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde70`](#insn-00bbde70)

~~~json
{
  "source": "00bbde70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde80`](#insn-00bbde80)

~~~json
{
  "source": "00bbde80",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde88`](#insn-00bbde88)

~~~json
{
  "source": "00bbde88",
  "target": "00bbe88c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbde98`](#insn-00bbde98)

~~~json
{
  "source": "00bbde98",
  "target": "00bbe88c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdea8`](#insn-00bbdea8)

~~~json
{
  "source": "00bbdea8",
  "target": "002fcb68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fcb68",
  "offset": 0,
  "size": 2,
  "datatype": "ushort",
  "bytes": "7901",
  "capture_start": "002fcb68",
  "capture_bytes": 2,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe498",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe88c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe644",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe928",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe960",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe670",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbdeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe69c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe9f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbebc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbeb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe874",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe22c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbdf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbec6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe2a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbecec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbea1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe1bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe418",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe974",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbea8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe4d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe14c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe6e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbeb0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe760",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbdfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbebec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbdf6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeb0`](#insn-00bbdeb0)

~~~json
{
  "source": "00bbdeb0",
  "target": "00bbe05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdec4`](#insn-00bbdec4)

~~~json
{
  "source": "00bbdec4",
  "target": "00bbdee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdeec`](#insn-00bbdeec)

~~~json
{
  "source": "00bbdeec",
  "target": "00bbdf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf08`](#insn-00bbdf08)

~~~json
{
  "source": "00bbdf08",
  "target": "00bbdf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf14`](#insn-00bbdf14)

~~~json
{
  "source": "00bbdf14",
  "target": "00bbe960",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf1c`](#insn-00bbdf1c)

~~~json
{
  "source": "00bbdf1c",
  "target": "00bbdf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf2c`](#insn-00bbdf2c)

~~~json
{
  "source": "00bbdf2c",
  "target": "00bbdf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf3c`](#insn-00bbdf3c)

~~~json
{
  "source": "00bbdf3c",
  "target": "00bbdf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf54`](#insn-00bbdf54)

~~~json
{
  "source": "00bbdf54",
  "target": "00bbe960",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf60`](#insn-00bbdf60)

~~~json
{
  "source": "00bbdf60",
  "target": "00bd1778",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf64`](#insn-00bbdf64)

~~~json
{
  "source": "00bbdf64",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf68`](#insn-00bbdf68)

~~~json
{
  "source": "00bbdf68",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf88`](#insn-00bbdf88)

~~~json
{
  "source": "00bbdf88",
  "target": "00bbdfa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdf90`](#insn-00bbdf90)

~~~json
{
  "source": "00bbdf90",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbdf94`](#insn-00bbdf94)

~~~json
{
  "source": "00bbdf94",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbdfc0`](#insn-00bbdfc0)

~~~json
{
  "source": "00bbdfc0",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbdfe8`](#insn-00bbdfe8)

~~~json
{
  "source": "00bbdfe8",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe008`](#insn-00bbe008)

~~~json
{
  "source": "00bbe008",
  "target": "00bbe028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe010`](#insn-00bbe010)

~~~json
{
  "source": "00bbe010",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe014`](#insn-00bbe014)

~~~json
{
  "source": "00bbe014",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe040`](#insn-00bbe040)

~~~json
{
  "source": "00bbe040",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe058`](#insn-00bbe058)

~~~json
{
  "source": "00bbe058",
  "target": "00bbed58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe078`](#insn-00bbe078)

~~~json
{
  "source": "00bbe078",
  "target": "00bbe098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe080`](#insn-00bbe080)

~~~json
{
  "source": "00bbe080",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe084`](#insn-00bbe084)

~~~json
{
  "source": "00bbe084",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe0b0`](#insn-00bbe0b0)

~~~json
{
  "source": "00bbe0b0",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe0c8`](#insn-00bbe0c8)

~~~json
{
  "source": "00bbe0c8",
  "target": "00bbe630",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe0e8`](#insn-00bbe0e8)

~~~json
{
  "source": "00bbe0e8",
  "target": "00bbe108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe0f0`](#insn-00bbe0f0)

~~~json
{
  "source": "00bbe0f0",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe0f4`](#insn-00bbe0f4)

~~~json
{
  "source": "00bbe0f4",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe120`](#insn-00bbe120)

~~~json
{
  "source": "00bbe120",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe144`](#insn-00bbe144)

~~~json
{
  "source": "00bbe144",
  "target": "0029365e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029365e",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "5f5f696e7431323800",
  "capture_start": "0029365e",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe148`](#insn-00bbe148)

~~~json
{
  "source": "00bbe148",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe168`](#insn-00bbe168)

~~~json
{
  "source": "00bbe168",
  "target": "00bbe188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe170`](#insn-00bbe170)

~~~json
{
  "source": "00bbe170",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe174`](#insn-00bbe174)

~~~json
{
  "source": "00bbe174",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1a0`](#insn-00bbe1a0)

~~~json
{
  "source": "00bbe1a0",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe1b8`](#insn-00bbe1b8)

~~~json
{
  "source": "00bbe1b8",
  "target": "00bbe9e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1d8`](#insn-00bbe1d8)

~~~json
{
  "source": "00bbe1d8",
  "target": "00bbe1f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe1e0`](#insn-00bbe1e0)

~~~json
{
  "source": "00bbe1e0",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe1e4`](#insn-00bbe1e4)

~~~json
{
  "source": "00bbe1e4",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe210`](#insn-00bbe210)

~~~json
{
  "source": "00bbe210",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe228`](#insn-00bbe228)

~~~json
{
  "source": "00bbe228",
  "target": "00bbe74c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe234`](#insn-00bbe234)

~~~json
{
  "source": "00bbe234",
  "target": "00bbe260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe244`](#insn-00bbe244)

~~~json
{
  "source": "00bbe244",
  "target": "00bbe260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe25c`](#insn-00bbe25c)

~~~json
{
  "source": "00bbe25c",
  "target": "00bbe88c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe264`](#insn-00bbe264)

~~~json
{
  "source": "00bbe264",
  "target": "00bc1ccc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe268`](#insn-00bbe268)

~~~json
{
  "source": "00bbe268",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe26c`](#insn-00bbe26c)

~~~json
{
  "source": "00bbe26c",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe274`](#insn-00bbe274)

~~~json
{
  "source": "00bbe274",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe280`](#insn-00bbe280)

~~~json
{
  "source": "00bbe280",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe28c`](#insn-00bbe28c)

~~~json
{
  "source": "00bbe28c",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe298`](#insn-00bbe298)

~~~json
{
  "source": "00bbe298",
  "target": "00bc1754",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe29c`](#insn-00bbe29c)

~~~json
{
  "source": "00bbe29c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2a0`](#insn-00bbe2a0)

~~~json
{
  "source": "00bbe2a0",
  "target": "00bbedf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2a4`](#insn-00bbe2a4)

~~~json
{
  "source": "00bbe2a4",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2c4`](#insn-00bbe2c4)

~~~json
{
  "source": "00bbe2c4",
  "target": "00bbe2e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2cc`](#insn-00bbe2cc)

~~~json
{
  "source": "00bbe2cc",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe2d0`](#insn-00bbe2d0)

~~~json
{
  "source": "00bbe2d0",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe2fc`](#insn-00bbe2fc)

~~~json
{
  "source": "00bbe2fc",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe314`](#insn-00bbe314)

~~~json
{
  "source": "00bbe314",
  "target": "00bbed58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe334`](#insn-00bbe334)

~~~json
{
  "source": "00bbe334",
  "target": "00bbe354",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe33c`](#insn-00bbe33c)

~~~json
{
  "source": "00bbe33c",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe340`](#insn-00bbe340)

~~~json
{
  "source": "00bbe340",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe36c`](#insn-00bbe36c)

~~~json
{
  "source": "00bbe36c",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe394`](#insn-00bbe394)

~~~json
{
  "source": "00bbe394",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe3b4`](#insn-00bbe3b4)

~~~json
{
  "source": "00bbe3b4",
  "target": "00bbe3d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe3bc`](#insn-00bbe3bc)

~~~json
{
  "source": "00bbe3bc",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe3c0`](#insn-00bbe3c0)

~~~json
{
  "source": "00bbe3c0",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe3ec`](#insn-00bbe3ec)

~~~json
{
  "source": "00bbe3ec",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe414`](#insn-00bbe414)

~~~json
{
  "source": "00bbe414",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe434`](#insn-00bbe434)

~~~json
{
  "source": "00bbe434",
  "target": "00bbe454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe43c`](#insn-00bbe43c)

~~~json
{
  "source": "00bbe43c",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe440`](#insn-00bbe440)

~~~json
{
  "source": "00bbe440",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe46c`](#insn-00bbe46c)

~~~json
{
  "source": "00bbe46c",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe494`](#insn-00bbe494)

~~~json
{
  "source": "00bbe494",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4a0`](#insn-00bbe4a0)

~~~json
{
  "source": "00bbe4a0",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4ac`](#insn-00bbe4ac)

~~~json
{
  "source": "00bbe4ac",
  "target": "00bbee08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4bc`](#insn-00bbe4bc)

~~~json
{
  "source": "00bbe4bc",
  "target": "00bbee38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4c8`](#insn-00bbe4c8)

~~~json
{
  "source": "00bbe4c8",
  "target": "00bbee08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4d0`](#insn-00bbe4d0)

~~~json
{
  "source": "00bbe4d0",
  "target": "00bbee74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4f0`](#insn-00bbe4f0)

~~~json
{
  "source": "00bbe4f0",
  "target": "00bbe510",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe4f8`](#insn-00bbe4f8)

~~~json
{
  "source": "00bbe4f8",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe4fc`](#insn-00bbe4fc)

~~~json
{
  "source": "00bbe4fc",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe528`](#insn-00bbe528)

~~~json
{
  "source": "00bbe528",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe540`](#insn-00bbe540)

~~~json
{
  "source": "00bbe540",
  "target": "00bbed58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe560`](#insn-00bbe560)

~~~json
{
  "source": "00bbe560",
  "target": "00bbe580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe568`](#insn-00bbe568)

~~~json
{
  "source": "00bbe568",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe56c`](#insn-00bbe56c)

~~~json
{
  "source": "00bbe56c",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe598`](#insn-00bbe598)

~~~json
{
  "source": "00bbe598",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe5c0`](#insn-00bbe5c0)

~~~json
{
  "source": "00bbe5c0",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5e0`](#insn-00bbe5e0)

~~~json
{
  "source": "00bbe5e0",
  "target": "00bbe600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe5e8`](#insn-00bbe5e8)

~~~json
{
  "source": "00bbe5e8",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe5ec`](#insn-00bbe5ec)

~~~json
{
  "source": "00bbe5ec",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe618`](#insn-00bbe618)

~~~json
{
  "source": "00bbe618",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe640`](#insn-00bbe640)

~~~json
{
  "source": "00bbe640",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe654`](#insn-00bbe654)

~~~json
{
  "source": "00bbe654",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe658`](#insn-00bbe658)

~~~json
{
  "source": "00bbe658",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe65c`](#insn-00bbe65c)

~~~json
{
  "source": "00bbe65c",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe668`](#insn-00bbe668)

~~~json
{
  "source": "00bbe668",
  "target": "00bd256c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe66c`](#insn-00bbe66c)

~~~json
{
  "source": "00bbe66c",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe680`](#insn-00bbe680)

~~~json
{
  "source": "00bbe680",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe684`](#insn-00bbe684)

~~~json
{
  "source": "00bbe684",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe688`](#insn-00bbe688)

~~~json
{
  "source": "00bbe688",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe694`](#insn-00bbe694)

~~~json
{
  "source": "00bbe694",
  "target": "00bd261c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe698`](#insn-00bbe698)

~~~json
{
  "source": "00bbe698",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6ac`](#insn-00bbe6ac)

~~~json
{
  "source": "00bbe6ac",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe6b0`](#insn-00bbe6b0)

~~~json
{
  "source": "00bbe6b0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6b4`](#insn-00bbe6b4)

~~~json
{
  "source": "00bbe6b4",
  "target": "00bbe898",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6bc`](#insn-00bbe6bc)

~~~json
{
  "source": "00bbe6bc",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe6c0`](#insn-00bbe6c0)

~~~json
{
  "source": "00bbe6c0",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6c4`](#insn-00bbe6c4)

~~~json
{
  "source": "00bbe6c4",
  "target": "00bbe898",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6d4`](#insn-00bbe6d4)

~~~json
{
  "source": "00bbe6d4",
  "target": "00bd4008",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe6d8`](#insn-00bbe6d8)

~~~json
{
  "source": "00bbe6d8",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6dc`](#insn-00bbe6dc)

~~~json
{
  "source": "00bbe6dc",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe6fc`](#insn-00bbe6fc)

~~~json
{
  "source": "00bbe6fc",
  "target": "00bbe71c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe704`](#insn-00bbe704)

~~~json
{
  "source": "00bbe704",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe708`](#insn-00bbe708)

~~~json
{
  "source": "00bbe708",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe734`](#insn-00bbe734)

~~~json
{
  "source": "00bbe734",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe75c`](#insn-00bbe75c)

~~~json
{
  "source": "00bbe75c",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe770`](#insn-00bbe770)

~~~json
{
  "source": "00bbe770",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe780`](#insn-00bbe780)

~~~json
{
  "source": "00bbe780",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7b8`](#insn-00bbe7b8)

~~~json
{
  "source": "00bbe7b8",
  "target": "00bbe7d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7cc`](#insn-00bbe7cc)

~~~json
{
  "source": "00bbe7cc",
  "target": "00bbe790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7dc`](#insn-00bbe7dc)

~~~json
{
  "source": "00bbe7dc",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe7e8`](#insn-00bbe7e8)

~~~json
{
  "source": "00bbe7e8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe800`](#insn-00bbe800)

~~~json
{
  "source": "00bbe800",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe808`](#insn-00bbe808)

~~~json
{
  "source": "00bbe808",
  "target": "00bbeeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe814`](#insn-00bbe814)

~~~json
{
  "source": "00bbe814",
  "target": "00bbeeb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe834`](#insn-00bbe834)

~~~json
{
  "source": "00bbe834",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe838`](#insn-00bbe838)

~~~json
{
  "source": "00bbe838",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe83c`](#insn-00bbe83c)

~~~json
{
  "source": "00bbe83c",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe848`](#insn-00bbe848)

~~~json
{
  "source": "00bbe848",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe854`](#insn-00bbe854)

~~~json
{
  "source": "00bbe854",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe86c`](#insn-00bbe86c)

~~~json
{
  "source": "00bbe86c",
  "target": "00bd1d54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe870`](#insn-00bbe870)

~~~json
{
  "source": "00bbe870",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe87c`](#insn-00bbe87c)

~~~json
{
  "source": "00bbe87c",
  "target": "00bbed8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe888`](#insn-00bbe888)

~~~json
{
  "source": "00bbe888",
  "target": "00bbed8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe894`](#insn-00bbe894)

~~~json
{
  "source": "00bbe894",
  "target": "00bd22b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe898`](#insn-00bbe898)

~~~json
{
  "source": "00bbe898",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8a4`](#insn-00bbe8a4)

~~~json
{
  "source": "00bbe8a4",
  "target": "00bbe918",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8c0`](#insn-00bbe8c0)

~~~json
{
  "source": "00bbe8c0",
  "target": "00bbe8d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8c8`](#insn-00bbe8c8)

~~~json
{
  "source": "00bbe8c8",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe8d0`](#insn-00bbe8d0)

~~~json
{
  "source": "00bbe8d0",
  "target": "00bbe904",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8d4`](#insn-00bbe8d4)

~~~json
{
  "source": "00bbe8d4",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe8dc`](#insn-00bbe8dc)

~~~json
{
  "source": "00bbe8dc",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe8e0`](#insn-00bbe8e0)

~~~json
{
  "source": "00bbe8e0",
  "target": "00bbf1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8e8`](#insn-00bbe8e8)

~~~json
{
  "source": "00bbe8e8",
  "target": "00bbe900",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe8f8`](#insn-00bbe8f8)

~~~json
{
  "source": "00bbe8f8",
  "target": "00bdb0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe924`](#insn-00bbe924)

~~~json
{
  "source": "00bbe924",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe930`](#insn-00bbe930)

~~~json
{
  "source": "00bbe930",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe944`](#insn-00bbe944)

~~~json
{
  "source": "00bbe944",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe954`](#insn-00bbe954)

~~~json
{
  "source": "00bbe954",
  "target": "002fcbdc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fcbdc",
  "offset": 0,
  "size": 2,
  "datatype": "ushort",
  "bytes": "7601",
  "capture_start": "002fcbdc",
  "capture_bytes": 2,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbef38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbf024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbeec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbe960",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbef24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbf0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbf14c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbf0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbeff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbf080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbf0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbf090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbf15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbefc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbf118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbef7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe95c`](#insn-00bbe95c)

~~~json
{
  "source": "00bbe95c",
  "target": "00bbefb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe968`](#insn-00bbe968)

~~~json
{
  "source": "00bbe968",
  "target": "00bd11d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe96c`](#insn-00bbe96c)

~~~json
{
  "source": "00bbe96c",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe970`](#insn-00bbe970)

~~~json
{
  "source": "00bbe970",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe990`](#insn-00bbe990)

~~~json
{
  "source": "00bbe990",
  "target": "00bbe9b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe998`](#insn-00bbe998)

~~~json
{
  "source": "00bbe998",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbe99c`](#insn-00bbe99c)

~~~json
{
  "source": "00bbe99c",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbe9c8`](#insn-00bbe9c8)

~~~json
{
  "source": "00bbe9c8",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbe9f0`](#insn-00bbe9f0)

~~~json
{
  "source": "00bbe9f0",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea04`](#insn-00bbea04)

~~~json
{
  "source": "00bbea04",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbea08`](#insn-00bbea08)

~~~json
{
  "source": "00bbea08",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea0c`](#insn-00bbea0c)

~~~json
{
  "source": "00bbea0c",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea14`](#insn-00bbea14)

~~~json
{
  "source": "00bbea14",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea18`](#insn-00bbea18)

~~~json
{
  "source": "00bbea18",
  "target": "00bbebac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea38`](#insn-00bbea38)

~~~json
{
  "source": "00bbea38",
  "target": "00bbea58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea40`](#insn-00bbea40)

~~~json
{
  "source": "00bbea40",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbea44`](#insn-00bbea44)

~~~json
{
  "source": "00bbea44",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbea70`](#insn-00bbea70)

~~~json
{
  "source": "00bbea70",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbea88`](#insn-00bbea88)

~~~json
{
  "source": "00bbea88",
  "target": "00bbecd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeaa8`](#insn-00bbeaa8)

~~~json
{
  "source": "00bbeaa8",
  "target": "00bbeac8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeab0`](#insn-00bbeab0)

~~~json
{
  "source": "00bbeab0",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbeab4`](#insn-00bbeab4)

~~~json
{
  "source": "00bbeab4",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeae0`](#insn-00bbeae0)

~~~json
{
  "source": "00bbeae0",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbeb08`](#insn-00bbeb08)

~~~json
{
  "source": "00bbeb08",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb28`](#insn-00bbeb28)

~~~json
{
  "source": "00bbeb28",
  "target": "00bbeb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb30`](#insn-00bbeb30)

~~~json
{
  "source": "00bbeb30",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbeb34`](#insn-00bbeb34)

~~~json
{
  "source": "00bbeb34",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb60`](#insn-00bbeb60)

~~~json
{
  "source": "00bbeb60",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbeb88`](#insn-00bbeb88)

~~~json
{
  "source": "00bbeb88",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeb9c`](#insn-00bbeb9c)

~~~json
{
  "source": "00bbeb9c",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbeba0`](#insn-00bbeba0)

~~~json
{
  "source": "00bbeba0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeba4`](#insn-00bbeba4)

~~~json
{
  "source": "00bbeba4",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeba8`](#insn-00bbeba8)

~~~json
{
  "source": "00bbeba8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbebb8`](#insn-00bbebb8)

~~~json
{
  "source": "00bbebb8",
  "target": "00bd24b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbebbc`](#insn-00bbebbc)

~~~json
{
  "source": "00bbebbc",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbebd0`](#insn-00bbebd0)

~~~json
{
  "source": "00bbebd0",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbebd4`](#insn-00bbebd4)

~~~json
{
  "source": "00bbebd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbebd8`](#insn-00bbebd8)

~~~json
{
  "source": "00bbebd8",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbebe4`](#insn-00bbebe4)

~~~json
{
  "source": "00bbebe4",
  "target": "00bd2404",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbebe8`](#insn-00bbebe8)

~~~json
{
  "source": "00bbebe8",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec08`](#insn-00bbec08)

~~~json
{
  "source": "00bbec08",
  "target": "00bbec28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec10`](#insn-00bbec10)

~~~json
{
  "source": "00bbec10",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbec14`](#insn-00bbec14)

~~~json
{
  "source": "00bbec14",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec40`](#insn-00bbec40)

~~~json
{
  "source": "00bbec40",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbec68`](#insn-00bbec68)

~~~json
{
  "source": "00bbec68",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec88`](#insn-00bbec88)

~~~json
{
  "source": "00bbec88",
  "target": "00bbeca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbec90`](#insn-00bbec90)

~~~json
{
  "source": "00bbec90",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbec94`](#insn-00bbec94)

~~~json
{
  "source": "00bbec94",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbecc0`](#insn-00bbecc0)

~~~json
{
  "source": "00bbecc0",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbece8`](#insn-00bbece8)

~~~json
{
  "source": "00bbece8",
  "target": "00bbed68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed08`](#insn-00bbed08)

~~~json
{
  "source": "00bbed08",
  "target": "00bbed28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed10`](#insn-00bbed10)

~~~json
{
  "source": "00bbed10",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbed14`](#insn-00bbed14)

~~~json
{
  "source": "00bbed14",
  "target": "00bbf1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed40`](#insn-00bbed40)

~~~json
{
  "source": "00bbed40",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "0029aafb",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "00290887",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290887",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "756e7369676e6564206c6f6e67206c6f6e6700",
  "capture_start": "00290887",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "002a91d2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a91d2",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "6c6f6e67206c6f6e6700",
  "capture_start": "002a91d2",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "00290870",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290870",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "77636861725f7400",
  "capture_start": "00290870",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "002ad7a7",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "00290878",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290878",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "756e7369676e65642073686f727400",
  "capture_start": "00290878",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "0029cf49",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029cf49",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "73686f727400",
  "capture_start": "0029cf49",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "0029d2a2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029d2a2",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "756e7369676e6564205f5f696e7431323800",
  "capture_start": "0029d2a2",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "002ad7ac",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad7ac",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "756e7369676e6564206c6f6e6700",
  "capture_start": "002ad7ac",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "00291536",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "002a730b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a730b",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "756e7369676e656420696e7400",
  "capture_start": "002a730b",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "00291806",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00291806",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "5f5f666c6f617431323800",
  "capture_start": "00291806",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "00297848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297848",
  "offset": 0,
  "size": 12,
  "datatype": "string",
  "bytes": "6c6f6e6720646f75626c6500",
  "capture_start": "00297848",
  "capture_bytes": 12,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "0029df19",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029df19",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "646f75626c6500",
  "capture_start": "0029df19",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "002a125f",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed68`](#insn-00bbed68)

~~~json
{
  "source": "00bbed68",
  "target": "002964e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed70`](#insn-00bbed70)

~~~json
{
  "source": "00bbed70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed74`](#insn-00bbed74)

~~~json
{
  "source": "00bbed74",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed78`](#insn-00bbed78)

~~~json
{
  "source": "00bbed78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed7c`](#insn-00bbed7c)

~~~json
{
  "source": "00bbed7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed98`](#insn-00bbed98)

~~~json
{
  "source": "00bbed98",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbed9c`](#insn-00bbed9c)

~~~json
{
  "source": "00bbed9c",
  "target": "00bc15e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbeda0`](#insn-00bbeda0)

~~~json
{
  "source": "00bbeda0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeda4`](#insn-00bbeda4)

~~~json
{
  "source": "00bbeda4",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedb0`](#insn-00bbedb0)

~~~json
{
  "source": "00bbedb0",
  "target": "00bbeeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedb8`](#insn-00bbedb8)

~~~json
{
  "source": "00bbedb8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedc0`](#insn-00bbedc0)

~~~json
{
  "source": "00bbedc0",
  "target": "00bbeeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedc4`](#insn-00bbedc4)

~~~json
{
  "source": "00bbedc4",
  "target": "00bbedd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedcc`](#insn-00bbedcc)

~~~json
{
  "source": "00bbedcc",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedd0`](#insn-00bbedd0)

~~~json
{
  "source": "00bbedd0",
  "target": "00bbede0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeddc`](#insn-00bbeddc)

~~~json
{
  "source": "00bbeddc",
  "target": "00bbfdf8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbede8`](#insn-00bbede8)

~~~json
{
  "source": "00bbede8",
  "target": "00bc1754",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbedec`](#insn-00bbedec)

~~~json
{
  "source": "00bbedec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbedf0`](#insn-00bbedf0)

~~~json
{
  "source": "00bbedf0",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee00`](#insn-00bbee00)

~~~json
{
  "source": "00bbee00",
  "target": "00bc1c24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee04`](#insn-00bbee04)

~~~json
{
  "source": "00bbee04",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee0c`](#insn-00bbee0c)

~~~json
{
  "source": "00bbee0c",
  "target": "00bc2f0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee10`](#insn-00bbee10)

~~~json
{
  "source": "00bbee10",
  "target": "00bbe898",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee1c`](#insn-00bbee1c)

~~~json
{
  "source": "00bbee1c",
  "target": "00bbeea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee28`](#insn-00bbee28)

~~~json
{
  "source": "00bbee28",
  "target": "00bbeea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee30`](#insn-00bbee30)

~~~json
{
  "source": "00bbee30",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee34`](#insn-00bbee34)

~~~json
{
  "source": "00bbee34",
  "target": "00bbee74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee40`](#insn-00bbee40)

~~~json
{
  "source": "00bbee40",
  "target": "00bbdd1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee44`](#insn-00bbee44)

~~~json
{
  "source": "00bbee44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee50`](#insn-00bbee50)

~~~json
{
  "source": "00bbee50",
  "target": "00bc2a60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee58`](#insn-00bbee58)

~~~json
{
  "source": "00bbee58",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee60`](#insn-00bbee60)

~~~json
{
  "source": "00bbee60",
  "target": "00bbeea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee6c`](#insn-00bbee6c)

~~~json
{
  "source": "00bbee6c",
  "target": "00bbeea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee7c`](#insn-00bbee7c)

~~~json
{
  "source": "00bbee7c",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee80`](#insn-00bbee80)

~~~json
{
  "source": "00bbee80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee84`](#insn-00bbee84)

~~~json
{
  "source": "00bbee84",
  "target": "00bbe898",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee94`](#insn-00bbee94)

~~~json
{
  "source": "00bbee94",
  "target": "00bd3d8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbee98`](#insn-00bbee98)

~~~json
{
  "source": "00bbee98",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbee9c`](#insn-00bbee9c)

~~~json
{
  "source": "00bbee9c",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeea4`](#insn-00bbeea4)

~~~json
{
  "source": "00bbeea4",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeea8`](#insn-00bbeea8)

~~~json
{
  "source": "00bbeea8",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeeac`](#insn-00bbeeac)

~~~json
{
  "source": "00bbeeac",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeeb0`](#insn-00bbeeb0)

~~~json
{
  "source": "00bbeeb0",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeeb4`](#insn-00bbeeb4)

~~~json
{
  "source": "00bbeeb4",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeec0`](#insn-00bbeec0)

~~~json
{
  "source": "00bbeec0",
  "target": "00bc136c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbeec4`](#insn-00bbeec4)

~~~json
{
  "source": "00bbeec4",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeefc`](#insn-00bbeefc)

~~~json
{
  "source": "00bbeefc",
  "target": "0029089a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029089a",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "206465636c74797065286175746f2900",
  "capture_start": "0029089a",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbeefc`](#insn-00bbeefc)

~~~json
{
  "source": "00bbeefc",
  "target": "002ac5ff",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac5ff",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "206175746f00",
  "capture_start": "002ac5ff",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbeefc`](#insn-00bbeefc)

~~~json
{
  "source": "00bbeefc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef04`](#insn-00bbef04)

~~~json
{
  "source": "00bbef04",
  "target": "00bbf39c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbef08`](#insn-00bbef08)

~~~json
{
  "source": "00bbef08",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef0c`](#insn-00bbef0c)

~~~json
{
  "source": "00bbef0c",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef1c`](#insn-00bbef1c)

~~~json
{
  "source": "00bbef1c",
  "target": "00bd1f4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbef20`](#insn-00bbef20)

~~~json
{
  "source": "00bbef20",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef2c`](#insn-00bbef2c)

~~~json
{
  "source": "00bbef2c",
  "target": "00bc2090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbef30`](#insn-00bbef30)

~~~json
{
  "source": "00bbef30",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef34`](#insn-00bbef34)

~~~json
{
  "source": "00bbef34",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef50`](#insn-00bbef50)

~~~json
{
  "source": "00bbef50",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef54`](#insn-00bbef54)

~~~json
{
  "source": "00bbef54",
  "target": "00bbef68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef64`](#insn-00bbef64)

~~~json
{
  "source": "00bbef64",
  "target": "00bbf190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef6c`](#insn-00bbef6c)

~~~json
{
  "source": "00bbef6c",
  "target": "00bc2f0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbef70`](#insn-00bbef70)

~~~json
{
  "source": "00bbef70",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef74`](#insn-00bbef74)

~~~json
{
  "source": "00bbef74",
  "target": "00bbf1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef78`](#insn-00bbef78)

~~~json
{
  "source": "00bbef78",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef88`](#insn-00bbef88)

~~~json
{
  "source": "00bbef88",
  "target": "00295789",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00295789",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "63686172385f7400",
  "capture_start": "00295789",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbef94`](#insn-00bbef94)

~~~json
{
  "source": "00bbef94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef98`](#insn-00bbef98)

~~~json
{
  "source": "00bbef98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbef9c`](#insn-00bbef9c)

~~~json
{
  "source": "00bbef9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefa0`](#insn-00bbefa0)

~~~json
{
  "source": "00bbefa0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefac`](#insn-00bbefac)

~~~json
{
  "source": "00bbefac",
  "target": "00bc9604",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbefb8`](#insn-00bbefb8)

~~~json
{
  "source": "00bbefb8",
  "target": "00bd1ff8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbefbc`](#insn-00bbefbc)

~~~json
{
  "source": "00bbefbc",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefc0`](#insn-00bbefc0)

~~~json
{
  "source": "00bbefc0",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefd4`](#insn-00bbefd4)

~~~json
{
  "source": "00bbefd4",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbefd8`](#insn-00bbefd8)

~~~json
{
  "source": "00bbefd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefdc`](#insn-00bbefdc)

~~~json
{
  "source": "00bbefdc",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbefe8`](#insn-00bbefe8)

~~~json
{
  "source": "00bbefe8",
  "target": "00bc6374",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbefec`](#insn-00bbefec)

~~~json
{
  "source": "00bbefec",
  "target": "00bbe89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbeffc`](#insn-00bbeffc)

~~~json
{
  "source": "00bbeffc",
  "target": "0029aaff",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029aaff",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "646563696d616c31323800",
  "capture_start": "0029aaff",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf008`](#insn-00bbf008)

~~~json
{
  "source": "00bbf008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf00c`](#insn-00bbf00c)

~~~json
{
  "source": "00bbf00c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf010`](#insn-00bbf010)

~~~json
{
  "source": "00bbf010",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf014`](#insn-00bbf014)

~~~json
{
  "source": "00bbf014",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf020`](#insn-00bbf020)

~~~json
{
  "source": "00bbf020",
  "target": "00bd1ca8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf038`](#insn-00bbf038)

~~~json
{
  "source": "00bbf038",
  "target": "00bbdd1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf03c`](#insn-00bbf03c)

~~~json
{
  "source": "00bbf03c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf048`](#insn-00bbf048)

~~~json
{
  "source": "00bbf048",
  "target": "00bc2a60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf050`](#insn-00bbf050)

~~~json
{
  "source": "00bbf050",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf058`](#insn-00bbf058)

~~~json
{
  "source": "00bbf058",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf064`](#insn-00bbf064)

~~~json
{
  "source": "00bbf064",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf078`](#insn-00bbf078)

~~~json
{
  "source": "00bbf078",
  "target": "00bd1e00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf07c`](#insn-00bbf07c)

~~~json
{
  "source": "00bbf07c",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf088`](#insn-00bbf088)

~~~json
{
  "source": "00bbf088",
  "target": "002a535f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a535f",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "646563696d616c333200",
  "capture_start": "002a535f",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf08c`](#insn-00bbf08c)

~~~json
{
  "source": "00bbf08c",
  "target": "00bbf0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf098`](#insn-00bbf098)

~~~json
{
  "source": "00bbf098",
  "target": "002a127d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a127d",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "6368617233325f7400",
  "capture_start": "002a127d",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf09c`](#insn-00bbf09c)

~~~json
{
  "source": "00bbf09c",
  "target": "00bbf124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0a8`](#insn-00bbf0a8)

~~~json
{
  "source": "00bbf0a8",
  "target": "002a91e6",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0ac`](#insn-00bbf0ac)

~~~json
{
  "source": "00bbf0ac",
  "target": "00bbf0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0b8`](#insn-00bbf0b8)

~~~json
{
  "source": "00bbf0b8",
  "target": "002a91dc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a91dc",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "646563696d616c363400",
  "capture_start": "002a91dc",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf0c8`](#insn-00bbf0c8)

~~~json
{
  "source": "00bbf0c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0cc`](#insn-00bbf0cc)

~~~json
{
  "source": "00bbf0cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0d0`](#insn-00bbf0d0)

~~~json
{
  "source": "00bbf0d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0d4`](#insn-00bbf0d4)

~~~json
{
  "source": "00bbf0d4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0e0`](#insn-00bbf0e0)

~~~json
{
  "source": "00bbf0e0",
  "target": "00bd1b50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf0ec`](#insn-00bbf0ec)

~~~json
{
  "source": "00bbf0ec",
  "target": "002925bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf0fc`](#insn-00bbf0fc)

~~~json
{
  "source": "00bbf0fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf100`](#insn-00bbf100)

~~~json
{
  "source": "00bbf100",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf104`](#insn-00bbf104)

~~~json
{
  "source": "00bbf104",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf108`](#insn-00bbf108)

~~~json
{
  "source": "00bbf108",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf114`](#insn-00bbf114)

~~~json
{
  "source": "00bbf114",
  "target": "00bc2bd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf120`](#insn-00bbf120)

~~~json
{
  "source": "00bbf120",
  "target": "002af7fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af7fc",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "6368617231365f7400",
  "capture_start": "002af7fc",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf130`](#insn-00bbf130)

~~~json
{
  "source": "00bbf130",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf134`](#insn-00bbf134)

~~~json
{
  "source": "00bbf134",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf138`](#insn-00bbf138)

~~~json
{
  "source": "00bbf138",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf13c`](#insn-00bbf13c)

~~~json
{
  "source": "00bbf13c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf148`](#insn-00bbf148)

~~~json
{
  "source": "00bbf148",
  "target": "00bd1bfc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf154`](#insn-00bbf154)

~~~json
{
  "source": "00bbf154",
  "target": "00291811",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00291811",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6465636c74797065286175746f2900",
  "capture_start": "00291811",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf158`](#insn-00bbf158)

~~~json
{
  "source": "00bbf158",
  "target": "00bbf168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf164`](#insn-00bbf164)

~~~json
{
  "source": "00bbf164",
  "target": "00295791",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00295791",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "7374643a3a6e756c6c7074725f7400",
  "capture_start": "00295791",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbf174`](#insn-00bbf174)

~~~json
{
  "source": "00bbf174",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf178`](#insn-00bbf178)

~~~json
{
  "source": "00bbf178",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf17c`](#insn-00bbf17c)

~~~json
{
  "source": "00bbf17c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf180`](#insn-00bbf180)

~~~json
{
  "source": "00bbf180",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf18c`](#insn-00bbf18c)

~~~json
{
  "source": "00bbf18c",
  "target": "00bd0280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf198`](#insn-00bbf198)

~~~json
{
  "source": "00bbf198",
  "target": "00bbdd1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf19c`](#insn-00bbf19c)

~~~json
{
  "source": "00bbf19c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1a8`](#insn-00bbf1a8)

~~~json
{
  "source": "00bbf1a8",
  "target": "00bc2a60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf1ac`](#insn-00bbf1ac)

~~~json
{
  "source": "00bbf1ac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1b8`](#insn-00bbf1b8)

~~~json
{
  "source": "00bbf1b8",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1c4`](#insn-00bbf1c4)

~~~json
{
  "source": "00bbf1c4",
  "target": "00bbf1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1dc`](#insn-00bbf1dc)

~~~json
{
  "source": "00bbf1dc",
  "target": "00bd1ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf1e0`](#insn-00bbf1e0)

~~~json
{
  "source": "00bbf1e0",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1e8`](#insn-00bbf1e8)

~~~json
{
  "source": "00bbf1e8",
  "target": "00bbed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbf1ec`](#insn-00bbf1ec)

~~~json
{
  "source": "00bbf1ec",
  "target": "00bdb1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbf1f0`](#insn-00bbf1f0)

~~~json
{
  "source": "00bbf1f0",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
