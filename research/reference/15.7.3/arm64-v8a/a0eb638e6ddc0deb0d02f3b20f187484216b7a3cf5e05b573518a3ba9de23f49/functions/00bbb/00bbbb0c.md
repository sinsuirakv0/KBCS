# 00bbbb0c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbbb0c",
  "name": "FUN_00bbbb0c",
  "size": 700,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "285d19dabedd3e61683e0f0dba2e7a2cb2e5dcacb240e2b33eb5cda88e22b1fb",
  "source_text_sha256": "285d19dabedd3e61683e0f0dba2e7a2cb2e5dcacb240e2b33eb5cda88e22b1fb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbbdc8](../00bbb/00bbbdc8.md)
- [00bbbebc](../00bbb/00bbbebc.md)
- [00bdb770](../00bdb/00bdb770.md)
- [00bde980](../00bde/00bde980.md)

## 疑似コード / UTF-8 5197 bytes

~~~c

ulong FUN_00bbbb0c(long param_1,long param_2,long *param_3)

{
  uint uVar1;
  int iVar2;
  long lVar3;
  long lVar4;
  ulong uVar5;
  long lVar6;
  char *__s2;
  long lVar7;
  long *local_98;
  undefined8 uStack_90;
  long local_88;
  undefined8 uStack_80;
  long local_78;
  undefined8 uStack_70;
  undefined8 local_68;
  undefined7 uStack_60;
  undefined1 local_59;
  undefined7 uStack_58;
  undefined8 uStack_51;
  undefined1 local_49;
  undefined8 local_48;
  
  __s2 = *(char **)(param_2 + 8);
  if (__s2 == PTR__ZTSDn_00c1c010) {
    *param_3 = 0;
    return 1;
  }
  uVar1 = *(uint *)(param_1 + 0x10);
  if ((uVar1 & 0x18) == 0) {
                    /* try { // try from 00bbbba4 to 00cbbbaf has its CatchHandler @ 00bbd21c */
    lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                           PTR__ZTIN10__cxxabiv117__pbase_type_infoE_00c1c008,0);
    if (lVar3 == 0) goto LAB_00bbbbc8;
                    /* try { // try from 00bbbbb0 to 00cbbbbf has its CatchHandler @ 00bbd208 */
    if ((*(byte *)(lVar3 + 0x10) & 0x18) == 0) {
                    /* try { // try from 00bbbbc0 to 00cbbbd3 has its CatchHandler @ 00bbd1f0 */
      if (*(char **)(param_1 + 8) != __s2) goto LAB_00bbbbc8;
      goto LAB_00bbbb6c;
    }
  }
                    /* try { // try from 00bbbb54 to 00cbbb5b has its CatchHandler @ 00bbd2e8 */
                    /* try { // try from 00bbbb5c to 00cbbb63 has its CatchHandler @ 00bbd220 */
  if ((param_1 == param_2) || (iVar2 = strcmp(*(char **)(param_1 + 8),__s2), iVar2 == 0)) {
LAB_00bbbb6c:
    if ((long *)*param_3 == (long *)0x0) {
      return 1;
    }
    *param_3 = *(long *)*param_3;
    return 1;
  }
LAB_00bbbbc8:
  lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                         PTR__ZTIN10__cxxabiv119__pointer_type_infoE_00c1c018,0);
  if (lVar3 == 0) {
    return 0;
  }
  if ((long *)*param_3 == (long *)0x0) {
    lVar6 = 0;
  }
  else {
    lVar6 = *(long *)*param_3;
    *param_3 = lVar6;
  }
  if (((*(uint *)(lVar3 + 0x10) & (uVar1 ^ 0xffffffff) & 7) == 0) &&
     ((uVar1 & (*(uint *)(lVar3 + 0x10) ^ 0xffffffff) & 0x60) == 0)) {
    lVar7 = *(long *)(param_1 + 0x18);
    lVar3 = *(long *)(lVar3 + 0x18);
    if (*(undefined **)(lVar7 + 8) == *(undefined **)(lVar3 + 8)) {
                    /* try { // try from 00bbbc94 to 00cbbca3 has its CatchHandler @ 00bbd3ec */
      return 1;
    }
    if (*(undefined **)(lVar7 + 8) == PTR__ZTSv_00c1c020) {
                    /* try { // try from 00bbbcb8 to 00cbbcbf has its CatchHandler @ 00bbd2e8 */
                    /* try { // try from 00bbbcc0 to 00cbbcc7 has its CatchHandler @ 00bbd1ec */
      lVar3 = __dynamic_cast(lVar3,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                             PTR__ZTIN10__cxxabiv120__function_type_infoE_00c1c028,0);
      return (ulong)(lVar3 == 0);
    }
                    /* try { // try from 00bbbc5c to 00cbbc67 has its CatchHandler @ 00bbd388 */
    lVar4 = __dynamic_cast(lVar7,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                           PTR__ZTIN10__cxxabiv119__pointer_type_infoE_00c1c018,0);
    if (lVar4 == 0) {
      lVar4 = __dynamic_cast(lVar7,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                             PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c030,0);
      if (lVar4 == 0) {
                    /* try { // try from 00bbbd20 to 00cbbd33 has its CatchHandler @ 00bbd1bc */
        local_88 = __dynamic_cast(lVar7,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                                  PTR__ZTIN10__cxxabiv117__class_type_infoE_00c1c000,0);
        if (local_88 == 0) {
          return 0;
        }
        local_98 = (long *)__dynamic_cast(lVar3,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                                          PTR__ZTIN10__cxxabiv117__class_type_infoE_00c1c000,0);
        if (local_98 != (long *)0x0) {
          local_49 = lVar6 != 0;
          local_48 = 0;
                    /* try { // try from 00bbbd6c to 00cbbd77 has its CatchHandler @ 00bbd2e8 */
                    /* try { // try from 00bbbd78 to 00cbbe53 has its CatchHandler @ 00bbd29c */
          uStack_90 = 0;
          uStack_58 = 0;
          uStack_70 = 0;
          local_78 = 0;
          uStack_60 = 0;
          local_59 = 0;
          local_68 = 0;
          uStack_51 = 0x100;
          uStack_80 = 0xffffffffffffffff;
          (**(code **)(*local_98 + 0x38))(local_98,&local_98,lVar6,1);
          if ((int)local_68 == 1) {
            if (lVar6 == 0) {
              local_78 = 0;
            }
            *param_3 = local_78;
            return 1;
          }
          return 0;
        }
        return 0;
      }
      if ((uVar1 & 1) != 0) {
                    /* try { // try from 00bbbd04 to 00cbbd0f has its CatchHandler @ 00bbd1e8 */
                    /* try { // try from 00bbbd10 to 00cbbd1f has its CatchHandler @ 00bbd1d4 */
        uVar5 = FUN_00bbbebc(lVar4,lVar3);
        return uVar5;
      }
    }
    else if ((uVar1 & 1) != 0) {
      uVar5 = FUN_00bbbdc8(lVar4,lVar3);
      return uVar5;
    }
  }
  return 0;
}

~~~
