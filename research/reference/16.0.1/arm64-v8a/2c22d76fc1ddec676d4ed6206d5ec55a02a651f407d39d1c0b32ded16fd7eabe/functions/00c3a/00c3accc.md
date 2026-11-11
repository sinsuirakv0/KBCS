# 00c3accc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00c3accc",
  "name": "FUN_00c3accc",
  "size": 5016,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d099741843a28e67ad746e91d4311acd03c31a2c9f213856c3f1742bc294d25d",
  "source_text_sha256": "d099741843a28e67ad746e91d4311acd03c31a2c9f213856c3f1742bc294d25d"
}
~~~

## 呼び出し元

- [00c39a80](../00c39/00c39a80.md)
- [00c3a178](../00c3a/00c3a178.md)
- [00c3accc](../00c3a/00c3accc.md)
- [00c3c940](../00c3c/00c3c940.md)
- [00c3fd7c](../00c3f/00c3fd7c.md)
- [00c41750](../00c41/00c41750.md)
- [00c42798](../00c42/00c42798.md)
- [00c429c0](../00c42/00c429c0.md)
- [00c42e90](../00c42/00c42e90.md)
- [00c46520](../00c46/00c46520.md)
- [00c47834](../00c47/00c47834.md)
- [00c4bb5c](../00c4b/00c4bb5c.md)
- [00c4e040](../00c4e/00c4e040.md)
- [00c4e5e8](../00c4e/00c4e5e8.md)
- [00c4ee68](../00c4e/00c4ee68.md)

## 呼び出し先

- [00c3ab8c](../00c3a/00c3ab8c.md)
- [00c3accc](../00c3a/00c3accc.md)
- [00c3c20c](../00c3c/00c3c20c.md)
- [00c3cc68](../00c3c/00c3cc68.md)
- [00c3e1dc](../00c3e/00c3e1dc.md)
- [00c3e454](../00c3e/00c3e454.md)
- [00c3e5c4](../00c3e/00c3e5c4.md)
- [00c3ea94](../00c3e/00c3ea94.md)
- [00c3eb3c](../00c3e/00c3eb3c.md)
- [00c3ef00](../00c3e/00c3ef00.md)
- [00c3f8d0](../00c3f/00c3f8d0.md)
- [00c3fa48](../00c3f/00c3fa48.md)
- [00c3fd7c](../00c3f/00c3fd7c.md)
- [00c431e4](../00c43/00c431e4.md)
- [00c46474](../00c46/00c46474.md)
- [00c4d0f0](../00c4d/00c4d0f0.md)
- [00c4e040](../00c4e/00c4e040.md)
- [00c4e5e8](../00c4e/00c4e5e8.md)
- [00c4e9c0](../00c4e/00c4e9c0.md)
- [00c4ea6c](../00c4e/00c4ea6c.md)
- [00c4eb18](../00c4e/00c4eb18.md)
- [00c4ebc4](../00c4e/00c4ebc4.md)
- [00c4ec70](../00c4e/00c4ec70.md)
- [00c4ed10](../00c4e/00c4ed10.md)
- [00c4edbc](../00c4e/00c4edbc.md)
- [00c4ee68](../00c4e/00c4ee68.md)
- [00c4f124](../00c4f/00c4f124.md)
- [00c4f274](../00c4f/00c4f274.md)
- [00c4f320](../00c4f/00c4f320.md)
- [00c4f3dc](../00c4f/00c4f3dc.md)
- [00c4f48c](../00c4f/00c4f48c.md)
- [00c50bfc](../00c50/00c50bfc.md)
- [00c50e78](../00c50/00c50e78.md)
- [00c57f40](../00c57/00c57f40.md)
- [00c58020](../00c58/00c58020.md)
- [00c5a020](../00c5a/00c5a020.md)
- [00c5a0a0](../00c5a/00c5a0a0.md)
- [00c5b140](../00c5b/00c5b140.md)

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

## 疑似コード / UTF-8 33279 bytes

~~~c

undefined8 * FUN_00c3accc(long *param_1)

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
  
                    /* try { // try from 00c3acd8 to 00d3acff has its CatchHandler @ 00c3acd8
                       catch() { ... } // from try @ 00c3acd8 with catch @ 00c3acd8
                       catch() { ... } // from try @ 00c3ad38 with catch @ 00c3acd8 */
  pcVar12 = (char *)*param_1;
  pbVar6 = (byte *)param_1[1];
  local_58 = (undefined8 *)0x0;
  uVar5 = (long)pbVar6 - (long)pcVar12;
  if (uVar5 == 0) goto code_r0x00c3b700;
  cVar1 = *pcVar12;
                    /* try { // try from 00c3ad00 to 00d3ad37 has its CatchHandler @ 00c3ad68 */
  switch(cVar1) {
  case 'A':
    pbVar13 = (byte *)(pcVar12 + 1);
    local_28 = 0;
    *param_1 = (long)pbVar13;
    if (pbVar6 == pbVar13) {
LAB_00c3bc78:
      uVar5 = FUN_00c3fd7c(param_1);
      puVar3 = (undefined8 *)0x0;
      if (uVar5 == 0) goto joined_r0x00c3bda0;
      pcVar12 = (char *)*param_1;
      if ((pcVar12 == (char *)param_1[1]) || (*pcVar12 != '_')) {
        return (undefined8 *)0x0;
      }
      pcVar12 = pcVar12 + 1;
      local_28 = uVar5;
    }
    else if (*pbVar13 - 0x3a < 0xfffffff6) {
      if (*pbVar13 != 0x5f) goto LAB_00c3bc78;
      pcVar12 = pcVar12 + 2;
    }
    else {
      local_50 = FUN_00c3ab8c(param_1,0);
      local_28 = FUN_00c3f8d0(param_1,local_50);
      pcVar12 = (char *)*param_1;
      if (pcVar12 == (char *)param_1[1]) {
        return (undefined8 *)0x0;
      }
      if (*pcVar12 != '_') {
        return (undefined8 *)0x0;
      }
      pcVar12 = pcVar12 + 1;
    }
    *param_1 = (long)pcVar12;
    pbVar6 = (byte *)FUN_00c3accc(param_1);
    puVar3 = (undefined8 *)0x0;
    local_50._0_8_ = pbVar6;
    if (pbVar6 != (byte *)0x0) {
      puVar3 = (undefined8 *)FUN_00c50bfc(param_1,local_50,&local_28);
    }
    goto joined_r0x00c3bda0;
  default:
    goto code_r0x00c3b700;
  case 'C':
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00c3accc(param_1);
    if ((byte *)local_50._0_8_ == (byte *)0x0) {
      return (undefined8 *)0x0;
    }
    puVar3 = (undefined8 *)FUN_00c4f3dc(param_1,local_50);
    goto LAB_00c3b70c;
  case 'D':
    if (uVar5 < 2) {
      return (undefined8 *)0x0;
    }
    cVar1 = pcVar12[1];
    puVar2 = (undefined8 *)0x0;
                    /* try { // try from 00c3b7ac to 00d3b7b3 has its CatchHandler @ 00c3b81c */
                    /* try { // try from 00c3b7b4 to 00d3b7d3 has its CatchHandler @ 00c3b6b8 */
    switch(cVar1) {
    case 'B':
    case 'U':
      pbVar13 = (byte *)(pcVar12 + 2);
      *param_1 = (long)pbVar13;
      local_28 = CONCAT71(local_28._1_7_,cVar1 == 'B');
      if ((pbVar6 == pbVar13) || (*pbVar13 - 0x3a < 0xfffffff6)) {
        local_50._0_8_ = FUN_00c3fd7c(param_1);
        if (local_50._0_8_ == 0) {
          return (undefined8 *)0x0;
        }
      }
      else {
        local_50 = FUN_00c3ab8c(param_1,0);
        lVar10 = FUN_00c3f8d0(param_1,local_50);
        local_50._0_8_ = lVar10;
      }
      pcVar12 = (char *)*param_1;
      if (pcVar12 == (char *)param_1[1]) {
        return (undefined8 *)0x0;
      }
      if (*pcVar12 != '_') {
        return (undefined8 *)0x0;
      }
      *param_1 = (long)(pcVar12 + 1);
      puVar3 = (undefined8 *)FUN_00c4ed10(param_1,local_50,&local_28);
      return puVar3;
    default:
      goto code_r0x00c3bbe0;
    case 'F':
      *param_1 = (long)(pcVar12 + 2);
      local_50 = FUN_00c3ab8c(param_1,0);
      uVar11 = FUN_00c3f8d0(param_1,local_50);
      pcVar12 = (char *)*param_1;
      if ((pcVar12 != (char *)param_1[1]) && (*pcVar12 == '_')) {
        *param_1 = (long)(pcVar12 + 1);
        local_50._0_8_ = uVar11;
        puVar3 = (undefined8 *)FUN_00c4ec70(param_1,local_50);
        return puVar3;
      }
      return (undefined8 *)0x0;
    case 'K':
    case 'k':
      local_50._0_8_ = " auto";
      if (cVar1 != 'k') {
        local_50._0_8_ = " decltype(auto)";
      }
      local_50._8_8_ = 5;
      if (cVar1 != 'k') {
        local_50._8_8_ = 0xf;
      }
      *param_1 = (long)(pcVar12 + 2);
      local_28 = FUN_00c3c20c(param_1,0);
      if (local_28 != 0) {
        puVar3 = (undefined8 *)FUN_00c4edbc(param_1,&local_28,local_50);
        return puVar3;
                    /* catch() { ... } // from try @ 00c3bb7c with catch @ 00c3bd90 */
      }
      return (undefined8 *)0x0;
    case 'O':
    case 'o':
    case 'w':
    case 'x':
      goto LAB_00c3b7d4;
    case 'T':
    case 't':
      puVar3 = (undefined8 *)FUN_00c3ef00(param_1);
      break;
    case 'a':
      puVar7 = &DAT_002a1d99;
      goto LAB_00c3bf60;
    case 'c':
      pcVar8 = "decltype(auto)";
      goto LAB_00c3bfd8;
    case 'd':
      pcVar8 = "decimal64";
      goto LAB_00c3bf2c;
    case 'e':
      *param_1 = (long)(pcVar12 + 2);
      puVar3 = (undefined8 *)FUN_00c4eb18(param_1,"decimal128");
      return puVar3;
    case 'f':
      pcVar8 = "decimal32";
LAB_00c3bf2c:
      *param_1 = (long)(pcVar12 + 2);
      puVar3 = (undefined8 *)FUN_00c4e9c0(param_1,pcVar8);
      return puVar3;
    case 'h':
      puVar7 = &DAT_002b9ebd;
LAB_00c3bf60:
      *param_1 = (long)(pcVar12 + 2);
                    /* catch() { ... } // from try @ 00c3c148 with catch @ 00c3bf6c */
      puVar3 = (undefined8 *)FUN_00c3fa48(param_1,puVar7);
      return puVar3;
    case 'i':
      pcVar8 = "char32_t";
      goto LAB_00c3bf94;
    case 'n':
      pcVar8 = "std::nullptr_t";
LAB_00c3bfd8:
      *param_1 = (long)(pcVar12 + 2);
      puVar3 = (undefined8 *)FUN_00c4d0f0(param_1,pcVar8);
      return puVar3;
    case 'p':
      *param_1 = (long)(pcVar12 + 2);
      local_50._0_8_ = FUN_00c3accc(param_1);
      if ((byte *)local_50._0_8_ == (byte *)0x0) {
        return (undefined8 *)0x0;
      }
      puVar3 = (undefined8 *)FUN_00c431e4(param_1,local_50);
      goto LAB_00c3b70c;
    case 's':
      pcVar8 = "char16_t";
LAB_00c3bf94:
      *param_1 = (long)(pcVar12 + 2);
      puVar3 = (undefined8 *)FUN_00c4ea6c(param_1,pcVar8);
      return puVar3;
    case 'u':
      *param_1 = (long)(pcVar12 + 2);
      puVar3 = (undefined8 *)FUN_00c46474(param_1,"char8_t");
      return puVar3;
    case 'v':
      puVar3 = (undefined8 *)FUN_00c4ee68(param_1);
    }
    goto joined_r0x00c3bda0;
  case 'F':
    goto LAB_00c3b7d4;
  case 'G':
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00c3accc(param_1);
    if ((byte *)local_50._0_8_ == (byte *)0x0) {
      return (undefined8 *)0x0;
    }
    puVar3 = (undefined8 *)FUN_00c4f48c(param_1,local_50);
    goto LAB_00c3b70c;
  case 'K':
  case 'V':
  case 'r':
    uVar15 = (ulong)(cVar1 == 'r');
    if (uVar15 < uVar5) {
                    /* try { // try from 00c3ad38 to 00d3ad97 has its CatchHandler @ 00c3acd8 */
      uVar14 = 1;
      if (cVar1 == 'r') {
        uVar14 = 2;
      }
      if (pcVar12[uVar15] != 'V') {
        uVar14 = (uint)(cVar1 == 'r');
      }
      uVar15 = (ulong)uVar14;
    }
    if (uVar15 < uVar5) {
                    /* catch() { ... } // from try @ 00c3ad00 with catch @ 00c3ad68 */
      uVar14 = (uint)uVar15;
      if (pcVar12[uVar15] == 'K') {
        uVar14 = uVar14 + 1;
      }
      uVar15 = (ulong)uVar14;
    }
                    /* try { // try from 00c3ad98 to 00d3adbf has its CatchHandler @ 00c3ad98
                       catch() { ... } // from try @ 00c3ad98 with catch @ 00c3ad98
                       catch() { ... } // from try @ 00c3adf8 with catch @ 00c3ad98 */
                    /* try { // try from 00c3adc0 to 00d3adf7 has its CatchHandler @ 00c3ae28 */
    if ((uVar5 <= uVar15) ||
       ((pcVar12[uVar15] != 'F' &&
        ((((pcVar12[uVar15] != 'D' || (uVar5 <= uVar15 + 1)) ||
          (0x29 < (byte)pcVar12[uVar15 + 1] - 0x4f)) ||
         ((1L << ((ulong)((byte)pcVar12[uVar15 + 1] - 0x4f) & 0x3f) & 0x30100000001U) == 0))))))
    goto code_r0x00c3adcc;
    goto LAB_00c3b7d4;
  case 'M':
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00c3accc(param_1);
    puVar3 = (undefined8 *)0x0;
    if ((byte *)local_50._0_8_ != (byte *)0x0) {
      local_28 = FUN_00c3accc(param_1);
      puVar3 = (undefined8 *)0x0;
      if (local_28 != 0) {
        puVar3 = (undefined8 *)FUN_00c50e78(param_1,local_50,&local_28);
      }
    }
    goto joined_r0x00c3bda0;
  case 'O':
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00c3accc(param_1);
    if ((byte *)local_50._0_8_ == (byte *)0x0) {
      return (undefined8 *)0x0;
    }
    local_28 = CONCAT44(local_28._4_4_,1);
    goto LAB_00c3ba1c;
  case 'P':
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00c3accc(param_1);
    if ((byte *)local_50._0_8_ == (byte *)0x0) {
      return (undefined8 *)0x0;
    }
    puVar3 = (undefined8 *)FUN_00c4f274(param_1,local_50);
    goto LAB_00c3b70c;
  case 'R':
    *param_1 = (long)(pcVar12 + 1);
    local_50._0_8_ = FUN_00c3accc(param_1);
    if ((byte *)local_50._0_8_ == (byte *)0x0) {
      return (undefined8 *)0x0;
    }
    local_28 = local_28 & 0xffffffff00000000;
LAB_00c3ba1c:
                    /* catch() { ... } // from try @ 00c3bc04 with catch @ 00c3ba28 */
    puVar3 = (undefined8 *)FUN_00c4f320(param_1,local_50,&local_28);
    goto LAB_00c3b70c;
  case 'S':
    if ((uVar5 < 2) || (pcVar12[1] != 't')) {
                    /* try { // try from 00c3bc04 to 00d3be5f has its CatchHandler @ 00c3ba28 */
      local_28 = (ulong)local_28._1_7_ << 8;
      puVar3 = (undefined8 *)FUN_00c3e454(param_1,0,&local_28);
      if (puVar3 == (undefined8 *)0x0) {
        return (undefined8 *)0x0;
      }
      local_58 = puVar3;
      if (((char *)param_1[1] == (char *)*param_1) || (*(char *)*param_1 != 'I')) {
        if ((local_28 & 0xff) != 0) {
          return puVar3;
        }
        goto LAB_00c3b70c;
      }
      if (((char)local_28 != '\0') && ((char)param_1[0x61] == '\0')) {
        return puVar3;
      }
      if ((char)local_28 == '\0') {
        FUN_00c3cc68(param_1 + 0x25,&local_58);
      }
      local_50._0_8_ = FUN_00c3e5c4(param_1,0);
      if ((byte *)local_50._0_8_ == (byte *)0x0) {
        return (undefined8 *)0x0;
      }
LAB_00c3bc64:
      puVar3 = (undefined8 *)FUN_00c3ea94(param_1,&local_58,local_50);
      goto LAB_00c3b70c;
    }
    goto code_r0x00c3b700;
  case 'T':
                    /* try { // try from 00c3b0ac to 00d3b137 has its CatchHandler @ 00c3b0ac
                       catch() { ... } // from try @ 00c3b0ac with catch @ 00c3b0ac
                       catch() { ... } // from try @ 00c3b140 with catch @ 00c3b0ac */
    if (((uVar5 < 2) || (0x10 < (byte)pcVar12[1] - 0x65)) ||
       ((1 << (ulong)((byte)pcVar12[1] - 0x65 & 0x1f) & 0x14001U) == 0)) {
      puVar3 = (undefined8 *)FUN_00c3eb3c(param_1);
      if (puVar3 == (undefined8 *)0x0) {
        return (undefined8 *)0x0;
      }
      local_58 = puVar3;
      if ((((char)param_1[0x61] == '\0') || ((char *)param_1[1] == (char *)*param_1)) ||
         (*(char *)*param_1 != 'I')) goto LAB_00c3b70c;
      local_50._0_8_ = FUN_00c3e5c4(param_1,0);
      if ((byte *)local_50._0_8_ == (byte *)0x0) {
        return (undefined8 *)0x0;
      }
      goto LAB_00c3bc64;
    }
code_r0x00c3b700:
    puVar3 = (undefined8 *)FUN_00c4f124(param_1);
    goto joined_r0x00c3bda0;
  case 'U':
code_r0x00c3adcc:
    puVar3 = (undefined8 *)FUN_00c4e5e8(param_1);
joined_r0x00c3bda0:
    if (puVar3 == (undefined8 *)0x0) {
      return (undefined8 *)0x0;
    }
LAB_00c3b70c:
    plVar18 = (long *)param_1[0x26];
    if (plVar18 == (long *)param_1[0x27]) {
      __src = (long *)param_1[0x25];
                    /* try { // try from 00c3b71c to 00d3b727 has its CatchHandler @ 00c3b81c */
      __n = (long)plVar18 - (long)__src;
                    /* try { // try from 00c3b728 to 00d3b74b has its CatchHandler @ 00c3b6b8 */
      if (__src == param_1 + 0x28) {
                    /* try { // try from 00c3b74c to 00d3b757 has its CatchHandler @ 00c3b81c */
        pvVar4 = malloc(__n * 2);
        if (pvVar4 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
          abort();
        }
                    /* try { // try from 00c3b758 to 00d3b77f has its CatchHandler @ 00c3b6b8 */
        if (plVar18 != __src) {
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
                    /* try { // try from 00c3b780 to 00d3b78b has its CatchHandler @ 00c3b81c */
      param_1[0x27] = (long)((long)pvVar4 + ((long)__n >> 2) * 8);
    }
                    /* try { // try from 00c3b78c to 00d3b7ab has its CatchHandler @ 00c3b6b8 */
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
LAB_00c3c05c:
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
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "signed char";
    goto LAB_00c3bb48;
  case 'b':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00c3b138 to 00d3b13f has its CatchHandler @ 00c3b1c4 */
      puVar3 = malloc(0x1000);
                    /* try { // try from 00c3b140 to 00d3b1ef has its CatchHandler @ 00c3b0ac */
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "bool";
    goto LAB_00c3bbc8;
  case 'c':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00c3bb7c to 00d3bc03 has its CatchHandler @ 00c3bd90 */
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "char";
    goto LAB_00c3bbc8;
  case 'd':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
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
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "long double";
LAB_00c3bb48:
    *(ushort *)((long)puVar2 + 9) = uVar9 & 0xf000 | 0x540;
    uVar11 = 0xb;
    break;
  case 'f':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "float";
    goto LAB_00c3b5bc;
  case 'g':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
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
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00c3b71c with catch @ 00c3b81c
                       catch(type#1 @ 00000000) { ... } // from try @ 00c3b74c with catch @ 00c3b81c
                       catch(type#1 @ 00000000) { ... } // from try @ 00c3b780 with catch @ 00c3b81c
                       catch(type#1 @ 00000000) { ... } // from try @ 00c3b7ac with catch @ 00c3b81c
                       catch(type#1 @ 00000000) { ... } // from try @ 00c3b7d4 with catch @ 00c3b81c
                        */
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "unsigned char";
    goto LAB_00c3b850;
  case 'i':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
                    /* try { // try from 00c3b45c to 00d3b463 has its CatchHandler @ 00c3b4e0 */
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
                    /* try { // try from 00c3b464 to 00d3b507 has its CatchHandler @ 00c3b3d0 */
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "int";
    goto LAB_00c3b4a0;
  case 'j':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
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
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "long";
    goto LAB_00c3bbc8;
  case 'm':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "unsigned long";
LAB_00c3b850:
    *(ushort *)((long)puVar2 + 9) = uVar9 & 0xf000 | 0x540;
    uVar11 = 0xd;
    break;
  case 'n':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    *(char **)((long)puVar3 + lVar10 + 0x20) = "__int128";
    *(undefined8 *)((long)puVar3 + lVar10 + 0x28) = 8;
    return puVar2;
  case 'o':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
                    /* try { // try from 00c3b3d0 to 00d3b45b has its CatchHandler @ 00c3b3d0
                       catch() { ... } // from try @ 00c3b3d0 with catch @ 00c3b3d0
                       catch() { ... } // from try @ 00c3b464 with catch @ 00c3b3d0 */
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "unsigned __int128";
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    uVar11 = 0x11;
    break;
  case 's':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "short";
LAB_00c3b5bc:
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
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "unsigned short";
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    uVar11 = 0xe;
    break;
  case 'u':
    pbVar13 = (byte *)(pcVar12 + 1);
    *param_1 = (long)pbVar13;
    if (pbVar6 == pbVar13) {
      return (undefined8 *)0x0;
    }
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
      local_50._8_8_ = (uVar15 + uVar16 * 10) - 0x30;
      if ((byte *)local_50._0_8_ == pbVar6) break;
      lVar10 = lVar17 + 1;
    } while (*(byte *)local_50._0_8_ - 0x30 < 10);
    if ((uVar5 - lVar17) - 2 < (ulong)local_50._8_8_) {
      return (undefined8 *)0x0;
    }
    pbVar13 = (byte *)(pcVar12 + uVar15 + uVar16 * 10 + lVar17 + -0x2e);
    *param_1 = (long)pbVar13;
    if (local_50._8_8_ == 0) {
      return (undefined8 *)0x0;
    }
    if ((pbVar13 == pbVar6) || (*pbVar13 != 0x49)) {
      puVar3 = (undefined8 *)FUN_00c3e1dc(param_1,local_50);
    }
    else {
      *param_1 = (long)(pcVar12 + uVar15 + uVar16 * 10 + lVar17 + -0x2d);
      local_28 = FUN_00c3accc(param_1);
      if (local_28 == 0) {
        return (undefined8 *)0x0;
      }
      pcVar12 = (char *)*param_1;
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00c3b728 with catch @ 00c3b6b8
                       catch(type#1 @ 00000000) { ... } // from try @ 00c3b758 with catch @ 00c3b6b8
                       catch(type#1 @ 00000000) { ... } // from try @ 00c3b78c with catch @ 00c3b6b8
                       catch(type#1 @ 00000000) { ... } // from try @ 00c3b7b4 with catch @ 00c3b6b8
                       catch(type#1 @ 00000000) { ... } // from try @ 00c3b7e0 with catch @ 00c3b6b8
                        */
      if (pcVar12 == (char *)param_1[1]) {
        return (undefined8 *)0x0;
      }
      if (*pcVar12 != 'E') {
        return (undefined8 *)0x0;
      }
      *param_1 = (long)(pcVar12 + 1);
      puVar3 = (undefined8 *)FUN_00c4ebc4(param_1,local_50,&local_28);
    }
    goto LAB_00c3b70c;
  case 'v':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
                    /* try { // try from 00c3ae80 to 00d3aeb7 has its CatchHandler @ 00c3aee8 */
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
                    /* try { // try from 00c3aeb8 to 00d3af17 has its CatchHandler @ 00c3ae58 */
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "void";
LAB_00c3bbc8:
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
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
                    /* catch() { ... } // from try @ 00c3b138 with catch @ 00c3b1c4 */
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
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
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
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
                    /* try { // try from 00c3adf8 to 00d3ae57 has its CatchHandler @ 00c3ad98 */
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
                    /* catch() { ... } // from try @ 00c3adc0 with catch @ 00c3ae28 */
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "unsigned long long";
    *(ushort *)((long)puVar3 + lVar10 + 0x19) =
         *(ushort *)((long)puVar3 + lVar10 + 0x19) & 0xf000 | 0x540;
    uVar11 = 0x12;
                    /* try { // try from 00c3ae58 to 00d3ae7f has its CatchHandler @ 00c3ae58
                       catch() { ... } // from try @ 00c3ae58 with catch @ 00c3ae58
                       catch() { ... } // from try @ 00c3aeb8 with catch @ 00c3ae58 */
    break;
  case 'z':
    pvVar4 = (void *)param_1[0x266];
    *param_1 = (long)(pcVar12 + 1);
    lVar10 = *(long *)((long)pvVar4 + 8);
                    /* catch() { ... } // from try @ 00c3ae80 with catch @ 00c3aee8 */
    puVar3 = pvVar4;
    if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
      puVar3 = malloc(0x1000);
      if (puVar3 == (void *)0x0) goto LAB_00c3c05c;
      lVar10 = 0;
      *puVar3 = pvVar4;
      puVar3[1] = 0;
      param_1[0x266] = (long)puVar3;
    }
    *(long *)((long)puVar3 + 8) = lVar10 + 0x20;
    puVar2 = (undefined8 *)((long)puVar3 + lVar10 + 0x10);
    *puVar2 = &PTR_FUN_00c97640;
    uVar9 = *(ushort *)((long)puVar3 + lVar10 + 0x19);
    *(undefined1 *)((long)puVar3 + lVar10 + 0x18) = 8;
    pcVar12 = "...";
LAB_00c3b4a0:
    *(ushort *)((long)puVar2 + 9) = uVar9 & 0xf000 | 0x540;
    uVar11 = 3;
  }
  puVar2[2] = pcVar12;
  puVar2[3] = uVar11;
code_r0x00c3bbe0:
  return puVar2;
LAB_00c3b7d4:
                    /* try { // try from 00c3b7d4 to 00d3b7df has its CatchHandler @ 00c3b81c */
  puVar3 = (undefined8 *)FUN_00c4e040(param_1);
  goto joined_r0x00c3bda0;
}

~~~
