# 00bbde5c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bbdd50`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) · [本文差分](../../changes/00bbde5c.md)
<!-- /kbcs-version-previous -->

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
  "source_text_sha256": "b767e72da1599fb1935953d11b4727c2b52e34ec85b07fcae82b79fe6657dfc7"
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
