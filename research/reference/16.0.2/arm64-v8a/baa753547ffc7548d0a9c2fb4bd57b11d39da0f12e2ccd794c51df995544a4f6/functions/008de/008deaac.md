# 008deaac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "008deaac",
  "name": "FUN_008deaac",
  "size": 2496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d65bac5cb592f0afb4886e5bcd17cc8837d7db9cb69926cb4d825527a89600b2",
  "source_text_sha256": "d65bac5cb592f0afb4886e5bcd17cc8837d7db9cb69926cb4d825527a89600b2"
}
~~~

## 呼び出し元

- [00859bb0](../00859/00859bb0.md)

## 呼び出し先

- [00467ba0](../00467/00467ba0.md)
- [00468c1c](../00468/00468c1c.md)
- [00468ca0](../00468/00468ca0.md)
- [00468fc8](../00468/00468fc8.md)
- [00469c44](../00469/00469c44.md)
- [0046af4c](../0046a/0046af4c.md)
- [0046ca04](../0046c/0046ca04.md)
- [0046cac4](../0046c/0046cac4.md)
- [0046d9b4](../0046d/0046d9b4.md)
- [0046d9ec](../0046d/0046d9ec.md)
- [00489f8c](../00489/00489f8c.md)
- [00498210](../00498/00498210.md)
- [00498844](../00498/00498844.md)
- [0077bb04](../0077b/0077bb04.md)
- [00851550](../00851/00851550.md)
- [00861508](../00861/00861508.md)
- [008dda58](../008dd/008dda58.md)
- [00acae1c](../00aca/00acae1c.md)
- [00b3bf30](../00b3b/00b3bf30.md)
- [00c57f00](../00c57/00c57f00.md)
- [00c57f20](../00c57/00c57f20.md)
- [00c57f40](../00c57/00c57f40.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c586e0](../00c58/00c586e0.md)

## 疑似コード / UTF-8 17240 bytes

~~~c

void FUN_008deaac(long param_1,undefined8 param_2)

{
  byte *pbVar1;
  int *piVar2;
  uint uVar3;
  int iVar4;
  int iVar5;
  long lVar6;
  uint uVar7;
  undefined *puVar8;
  int iVar9;
  int iVar10;
  undefined4 uVar11;
  long lVar12;
  long lVar13;
  ulong uVar14;
  undefined8 uVar15;
  float fVar16;
  undefined1 auStack_7c [20];
  long local_68;
  
  lVar6 = tpidr_el0;
  local_68 = *(long *)(lVar6 + 0x28);
  if (((DAT_00ca5038 & 1) == 0) && (iVar9 = __cxa_guard_acquire(&DAT_00ca5038), iVar9 != 0)) {
    DAT_00ca5008 = 0;
    DAT_00ca5000 = &DAT_00ca5008;
    DAT_00ca5028 = 0;
    DAT_00ca5030 = 0;
    DAT_00ca5020 = 0;
    DAT_00ca5010 = 0;
    DAT_00ca5018 = &DAT_00ca5020;
    __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
    __cxa_guard_release(&DAT_00ca5038);
  }
  if (DAT_00ca5030 != 0) {
    FUN_00498210();
  }
  pbVar1 = (byte *)((long)&fde_table_entry_00332060.initial_loc + param_1);
  piVar2 = (int *)((long)&fde_table_entry_00333cc8.data_loc + param_1);
  if (DAT_00ca4a78 == 0) {
    lVar12 = 0;
  }
  else {
    lVar12 = __dynamic_cast(DAT_00ca4a78,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                            &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c85168,0);
  }
  iVar9 = FUN_0046ca04(param_1);
  lVar13 = FUN_00489f8c(*(undefined8 *)(lVar12 + 0xf8),0xb);
  iVar9 = iVar9 - *(int *)(lVar13 + 8);
  if (*(char *)(lVar12 + 0x2f0) == '\0') {
LAB_008deb88:
    *(undefined1 *)(lVar12 + 0x2f0) = 0;
    FUN_00467ba0(param_2,0x58,0xb8,0xcc,0xff);
    uVar15 = *(undefined8 *)(lVar12 + 0x128);
                    /* try { // try from 008debac to 009debb7 has its CatchHandler @ 008df020 */
    iVar10 = FUN_0046ca04(param_1);
    FUN_00851550();
    uVar11 = FUN_0046cac4();
                    /* try { // try from 008debcc to 009debe7 has its CatchHandler @ 008df028 */
    FUN_00469c44(param_2,uVar15,0xffffffd8,0,iVar10 + 0x50,uVar11,0x4c);
                    /* try { // try from 008debe8 to 009deeb3 has its CatchHandler @ 008de918 */
    FUN_00467ba0(param_2,0x6c,200,0xce,0xff);
    fVar16 = (float)FUN_0046d9ec((float)*(int *)((long)&fde_table_entry_00333f98.data_loc + param_1)
                                );
    FUN_00468c1c(param_2,(int)(fVar16 * 115.0) + 0x8c);
    uVar15 = *(undefined8 *)(lVar12 + 0x118);
    uVar11 = FUN_0046ca04(param_1);
    FUN_00469c44(param_2,uVar15,0,0,uVar11,0x330,0);
    FUN_00468c1c(param_2,0xff);
    FUN_00467ba0(param_2,0xff,0xff,0xff,0xff);
    FUN_008dda58(param_1 + 0x2158);
    FUN_00468ca0(param_2,0);
    FUN_00861508(param_1,*(undefined8 *)(lVar12 + 200),0,0);
    uVar15 = *(undefined8 *)(lVar12 + 200);
    uVar11 = FUN_0046ca04(param_1);
    FUN_00469c44(param_2,uVar15,0,0,uVar11,0x37,0);
    FUN_00467ba0(param_2,0xff,0xff,0xff,0xff);
    FUN_00468c1c(param_2,0x72);
    if (0 < **(int **)(param_1 + 0x21d8)) {
      uVar15 = *(undefined8 *)(lVar12 + 0xa8);
      lVar13 = FUN_00851550();
      fVar16 = (float)FUN_0046d9b4((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   lVar13) * 0x1e));
      FUN_00468fc8(param_2,uVar15,(int)(fVar16 * 10.0 + 24.0),0xff,8);
    }
    FUN_00468ca0(param_2,1);
    iVar10 = **(int **)(param_1 + 0x21d8);
    lVar13 = FUN_00851550();
    if (iVar10 < *(int *)((long)&fde_table_entry_00335f78.initial_loc + lVar13) + -1) {
      uVar15 = *(undefined8 *)(lVar12 + 0xa8);
      iVar10 = FUN_0046ca04(param_1);
      lVar13 = FUN_00851550();
      fVar16 = (float)FUN_0046d9b4((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   lVar13) * 0x1e));
      FUN_00468fc8(param_2,uVar15,(int)((float)(iVar10 + -0x56) + fVar16 * -10.0),0xff,8);
    }
    FUN_00468ca0(param_2,0);
    FUN_00468c1c(param_2,0xff);
    iVar10 = *(int *)((long)&fde_table_entry_00334170.data_loc + param_1);
    if (iVar10 < 0x129) {
      FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0x1f8),8 - iVar10,3,1);
    }
    if (((((((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) == 0) &&
           ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) == 0)) &&
          ((*(byte *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 1) & 1) == 0)) &&
         (((*(byte *)((long)&fde_table_entry_00332a28.initial_loc + param_1 + 1) & 1) == 0 &&
          ((*(byte *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) & 1) == 0)))) &&
        ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 2) & 1) == 0)) &&
       (((*pbVar1 & 1) == 0 &&
        (*(char *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 2) != '\0')))) {
      uVar3 = *(uint *)((long)&fde_table_entry_00333f98.initial_loc + param_1);
      uVar7 = -uVar3;
      uVar3 = uVar3 & 3;
      if (-1 < (int)uVar7) {
        uVar3 = -(uVar7 & 3);
      }
      FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),3,0x21c,0x60,0x60,
                   ((uint)(int)(char)((char)uVar3 + (char)((uVar3 & 0x80) >> 7)) >> 1) + 0xc & 0xff)
      ;
    }
    FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0xf8),iVar9,0,0xb);
                    /* try { // try from 008deeb4 to 009deebf has its CatchHandler @ 008deff4 */
    FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0xf8),iVar9 + -100,0x11,10);
    uVar15 = *(undefined8 *)(lVar12 + 0xf8);
                    /* try { // try from 008deec4 to 009deee3 has its CatchHandler @ 008defe4 */
    iVar10 = FUN_0046ca04(param_1);
    uVar11 = FUN_00b3bf30(param_1 + 0xc570);
                    /* try { // try from 008deee4 to 009df07b has its CatchHandler @ 008de918 */
    FUN_0046af4c(auStack_7c,(float)(iVar10 + -6),0x40c00000,0xbf800000,param_2,uVar15,0,uVar11,0,0,2
                 ,0);
    FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),iVar9 + -0x25,8,0x3e,0x24,0x17);
  }
  else {
    if (((DAT_00ca5038 & 1) == 0) && (iVar10 = __cxa_guard_acquire(&DAT_00ca5038), iVar10 != 0)) {
      DAT_00ca5008 = 0;
      DAT_00ca5000 = &DAT_00ca5008;
      DAT_00ca5028 = 0;
      DAT_00ca5030 = 0;
      DAT_00ca5020 = 0;
      DAT_00ca5010 = 0;
      DAT_00ca5018 = &DAT_00ca5020;
      __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
      __cxa_guard_release(&DAT_00ca5038);
    }
    if ((DAT_00ca5030 == 0) || (uVar14 = FUN_00498844(), (uVar14 & 1) != 0)) goto LAB_008deb88;
  }
  FUN_00acae1c((long)&fde_table_entry_00337d90.initial_loc + param_1,*(undefined8 *)(lVar12 + 0x1a8)
               ,0);
  if ((((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) != 0) ||
      ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) != 0)) ||
     (*(char *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) != '\0')) {
    FUN_00861508(param_1,*(undefined8 *)(lVar12 + 200),0,0);
    uVar15 = *(undefined8 *)(lVar12 + 200);
    uVar11 = FUN_0046ca04(param_1);
    FUN_00469c44(param_2,uVar15,0,0,uVar11,0x37,0);
    iVar10 = *(int *)((long)&fde_table_entry_00334170.data_loc + param_1);
    if (iVar10 < 0x129) {
      FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0x1f8),8 - iVar10,3,1);
    }
  }
  FUN_00468ca0(param_2,2);
  uVar15 = *(undefined8 *)(lVar12 + 200);
  uVar11 = FUN_0046ca04(param_1);
                    /* catch() { ... } // from try @ 008deec4 with catch @ 008defe4 */
                    /* catch() { ... } // from try @ 008deeb4 with catch @ 008deff4 */
  FUN_00469c44(param_2,uVar15,0,0x249,uVar11,0x37,0);
                    /* catch() { ... } // from try @ 008de9f0 with catch @ 008deffc */
  FUN_00468ca0(param_2,0);
  puVar8 = PTR_DAT_00c9b578;
                    /* catch() { ... } // from try @ 008debac with catch @ 008df020 */
  iVar4 = *(int *)(PTR_DAT_00c9b578 +
                  (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) * 4);
                    /* catch() { ... } // from try @ 008debcc with catch @ 008df028 */
  iVar10 = iVar4;
  if (iVar4 < 0) {
    iVar10 = iVar4 + 1;
  }
  FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),*piVar2 - (iVar10 >> 1),
               *(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar10 >> 1),
               *(int *)((long)&fde_table_entry_00333cd0.data_loc + param_1) + iVar4,
               *(int *)((long)&fde_table_entry_00333cd8.initial_loc + param_1) + iVar4,9);
  iVar5 = *(int *)(puVar8 + (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) *
                            4);
  iVar10 = iVar5 + 0x54;
  iVar4 = iVar5 + 0x3c;
  if (iVar5 < 0) {
    iVar5 = iVar5 + 1;
  }
                    /* try { // try from 008df07c to 009df0c3 has its CatchHandler @ 008df07c
                       catch() { ... } // from try @ 008df07c with catch @ 008df07c
                       catch() { ... } // from try @ 008df0dc with catch @ 008df07c */
  FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),(*piVar2 - (iVar5 >> 1)) + 4,
               (*(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar5 >> 1)) +
               0x11,iVar10,iVar4,3);
  if (((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) == 0) &&
     ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) == 0)) {
    if (((((*(byte *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 1) & 1) == 0) &&
         (((*(byte *)((long)&fde_table_entry_00332a28.initial_loc + param_1 + 1) & 1) == 0 &&
          ((*(byte *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) & 1) == 0)))) &&
        ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 2) & 1) == 0)) &&
       (((*pbVar1 & 1) == 0 &&
        (*(char *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 2) != '\0')))) {
      uVar3 = *(uint *)((long)&fde_table_entry_00333f98.initial_loc + param_1);
      uVar7 = -uVar3;
      uVar3 = uVar3 & 3;
      if (-1 < (int)uVar7) {
        uVar3 = -(uVar7 & 3);
      }
      FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),3,0x21c,0x60,0x60,
                   ((uint)(int)(char)((char)uVar3 + (char)((uVar3 & 0x80) >> 7)) >> 1) + 0xc & 0xff)
      ;
      if (*(char *)((long)&fde_table_entry_00332a20.data_loc + param_1) == '\0' &&
          *(char *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) == '\0') {
LAB_008df0cc:
        if (*(char *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) == '\0')
        goto LAB_008df178;
      }
    }
    else {
                    /* try { // try from 008df0c4 to 009df0db has its CatchHandler @ 008df110 */
      if (*(char *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) == '\0')
      goto LAB_008df0cc;
    }
  }
                    /* try { // try from 008df0dc to 009df13f has its CatchHandler @ 008df07c */
  FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0xf8),iVar9,0,0xb);
  FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0xf8),iVar9 + -100,0x11,10);
  uVar15 = *(undefined8 *)(lVar12 + 0xf8);
  iVar10 = FUN_0046ca04(param_1);
                    /* catch() { ... } // from try @ 008df0c4 with catch @ 008df110 */
  uVar11 = FUN_00b3bf30(param_1 + 0xc570);
                    /* try { // try from 008df140 to 009e348b has its CatchHandler @ 008df140
                       catch() { ... } // from try @ 008df140 with catch @ 008df140
                       catch() { ... } // from try @ 008e34b8 with catch @ 008df140
                       catch() { ... } // from try @ 008e53d4 with catch @ 008df140
                       catch() { ... } // from try @ 008e6074 with catch @ 008df140
                       catch() { ... } // from try @ 008e6110 with catch @ 008df140
                       catch() { ... } // from try @ 008e6218 with catch @ 008df140
                       catch() { ... } // from try @ 008e62b4 with catch @ 008df140
                       catch() { ... } // from try @ 008e78d0 with catch @ 008df140
                       catch() { ... } // from try @ 008e7b28 with catch @ 008df140
                       catch() { ... } // from try @ 008e7c3c with catch @ 008df140
                       catch() { ... } // from try @ 008e7f54 with catch @ 008df140
                       catch() { ... } // from try @ 008e94b0 with catch @ 008df140
                       catch() { ... } // from try @ 008eadb0 with catch @ 008df140
                       catch() { ... } // from try @ 008eae20 with catch @ 008df140
                       catch() { ... } // from try @ 008eae8c with catch @ 008df140
                       catch() { ... } // from try @ 008eaef8 with catch @ 008df140
                       catch() { ... } // from try @ 008eb0a4 with catch @ 008df140
                       catch() { ... } // from try @ 008eb118 with catch @ 008df140
                       catch() { ... } // from try @ 008eb180 with catch @ 008df140
                       catch() { ... } // from try @ 008eb1e8 with catch @ 008df140
                       catch() { ... } // from try @ 008eb2a8 with catch @ 008df140
                       catch() { ... } // from try @ 008eb314 with catch @ 008df140
                       catch() { ... } // from try @ 008eb37c with catch @ 008df140
                       catch() { ... } // from try @ 008eb3e4 with catch @ 008df140
                       catch() { ... } // from try @ 008eb8dc with catch @ 008df140
                       catch() { ... } // from try @ 008eb94c with catch @ 008df140
                       catch() { ... } // from try @ 008eb9b8 with catch @ 008df140
                       catch() { ... } // from try @ 008eba24 with catch @ 008df140
                       catch() { ... } // from try @ 008ebc34 with catch @ 008df140
                       catch() { ... } // from try @ 008ebcd4 with catch @ 008df140
                       catch() { ... } // from try @ 008ec030 with catch @ 008df140
                       catch() { ... } // from try @ 008eccd8 with catch @ 008df140
                       catch() { ... } // from try @ 008ece58 with catch @ 008df140
                       catch() { ... } // from try @ 008ed218 with catch @ 008df140
                       catch() { ... } // from try @ 008ede1c with catch @ 008df140
                       catch() { ... } // from try @ 008ee208 with catch @ 008df140
                       catch() { ... } // from try @ 008ee2d4 with catch @ 008df140
                       catch() { ... } // from try @ 008ee2f8 with catch @ 008df140
                       catch() { ... } // from try @ 008ef098 with catch @ 008df140 */
  FUN_0046af4c(auStack_7c,(float)(iVar10 + -6),0x40c00000,0xbf800000,param_2,uVar15,0,uVar11,0,0,2,0
              );
  FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),iVar9 + -0x25,8,0x3e,0x24,0x17);
LAB_008df178:
  FUN_00468ca0(param_2,2);
  FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0xf8),iVar9,0x249,0xb);
  FUN_00468ca0(param_2,0);
  FUN_0077bb04(param_1,param_2,*(undefined8 *)(lVar12 + 0xa8),iVar9,1,0);
  uVar15 = *(undefined8 *)(lVar12 + 0xf8);
  iVar9 = FUN_0046ca04(param_1);
  uVar11 = FUN_00b3bf30(param_1 + 0xc400);
  FUN_0046af4c(auStack_7c,(float)(iVar9 + -6),0x44140000,0xbf800000,param_2,uVar15,0,uVar11,0,0,2,0)
  ;
  iVar10 = *(int *)(puVar8 + (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) *
                             4);
  iVar9 = iVar10;
  if (iVar10 < 0) {
    iVar9 = iVar10 + 1;
  }
  FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),*piVar2 - (iVar9 >> 1),
               *(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar9 >> 1),
               *(int *)((long)&fde_table_entry_00333cd0.data_loc + param_1) + iVar10,
               *(int *)((long)&fde_table_entry_00333cd8.initial_loc + param_1) + iVar10,9);
  iVar4 = *(int *)(puVar8 + (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) *
                            4);
  iVar9 = iVar4 + 0x54;
  iVar10 = iVar4 + 0x3c;
  if (iVar4 < 0) {
    iVar4 = iVar4 + 1;
  }
  FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),(*piVar2 - (iVar4 >> 1)) + 4,
               (*(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar4 >> 1)) +
               0x11,iVar9,iVar10,3);
  if (((((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) == 0) &&
       ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) == 0)) &&
      ((*(byte *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 1) & 1) == 0)) &&
     ((((*(byte *)((long)&fde_table_entry_00332a28.initial_loc + param_1 + 1) & 1) == 0 &&
       ((*(byte *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) & 1) == 0)) &&
      (((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 2) & 1) == 0 &&
       (((*pbVar1 & 1) == 0 &&
        (*(char *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 2) != '\0')))))))) {
    uVar3 = *(uint *)((long)&fde_table_entry_00333f98.initial_loc + param_1);
    uVar7 = -uVar3;
    uVar3 = uVar3 & 3;
    if (-1 < (int)uVar7) {
      uVar3 = -(uVar7 & 3);
    }
    FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),3,0x21c,0x60,0x60,
                 ((uint)(int)(char)((char)uVar3 + (char)((uVar3 & 0x80) >> 7)) >> 1) + 0xc & 0xff);
  }
  if (*(long *)(lVar6 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
