# 00bb5ffc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bb5ffc.md)

## 関数情報

~~~json
{
  "address": "00bb5ffc",
  "name": "FUN_00bb5ffc",
  "size": 1324,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e36e4d631ed1c6a96edd0a93b57b6d9db4d074eb9149b340c5216f4a11ac3b24",
  "source_text_sha256": "e36e4d631ed1c6a96edd0a93b57b6d9db4d074eb9149b340c5216f4a11ac3b24"
}
~~~
## 呼び出し元

- [00bb5c14](../00bb5/00bb5c14.md)
- [00bb6528](../00bb6/00bb6528.md)

## 呼び出し先

- [00bb9248](../00bb9/00bb9248.md)
- [00bdb0f0](../00bdb/00bdb0f0.md)
- [00bdb7b0](../00bdb/00bdb7b0.md)
- [00be0fe0](../00be0/00be0fe0.md)

## 疑似コード 1/1 / UTF-8 9023 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00bb5ffc(undefined4 *param_1,byte *param_2,ulong param_3,char param_4,char param_5,
                 byte param_6)

{
  ulong uVar1;
  byte bVar2;
  size_t __n;
  byte *pbVar3;
  bool bVar4;
  undefined2 uVar5;
  long lVar6;
  long lVar7;
  byte *pbVar8;
  byte *pbVar10;
  long lVar11;
  byte *pbVar12;
  byte *pbVar13;
  byte *pbVar9;
  
  if ((param_3 & 1) == 0) {
    bVar4 = false;
  }
  else {
    uVar1 = (ulong)(*param_2 >> 1);
    if ((*param_2 & 1) != 0) {
      uVar1 = *(ulong *)(param_2 + 8);
    }
    bVar4 = uVar1 == 4;
  }
                    /* try { // try from 00bb6040 to 00cb604b has its CatchHandler @ 00bbabc4 */
  if (param_4 == '\x01') {
    if (param_6 < 2) {
      if (param_6 == 0) {
        *param_1 = (int)DAT_002b2708;
joined_r0x00bb61d0:
        if (param_5 == '\0') {
          return;
        }
        if (param_5 == '\x02') {
          return;
        }
        if (param_5 != '\x01') goto LAB_00bb63c4;
        goto joined_r0x00bb63bc;
      }
      if (param_6 != 1) goto LAB_00bb63c4;
      *(undefined1 *)param_1 = 3;
      *(undefined1 *)((long)param_1 + 3) = 4;
    }
    else {
      if (param_6 == 2) {
        *(undefined1 *)param_1 = 2;
        *(undefined1 *)((long)param_1 + 3) = 3;
                    /* try { // try from 00bb6170 to 00cb617f has its CatchHandler @ 00bbada0 */
        if (param_5 == '\x02') {
                    /* try { // try from 00bb6438 to 00cb6443 has its CatchHandler @ 00bbade8 */
          uVar5 = 0x104;
          goto LAB_00bb643c;
        }
        if (param_5 != '\x01') {
          if (param_5 == '\0') {
            *(undefined2 *)((long)param_1 + 1) = 0x400;
            return;
          }
          goto LAB_00bb63c4;
        }
                    /* try { // try from 00bb6420 to 00cb642f has its CatchHandler @ 00bbade4 */
        uVar5 = 0x400;
        goto LAB_00bb64bc;
      }
      if (param_6 != 3) {
        if (param_6 == 4) {
          *(undefined1 *)param_1 = 2;
          *(undefined1 *)((long)param_1 + 3) = 4;
          if (param_5 == '\x02') {
            uVar5 = 0x300;
            goto LAB_00bb64bc;
          }
                    /* try { // try from 00bb610c to 00cb6117 has its CatchHandler @ 00bbacb0 */
          if (param_5 == '\x01') {
            uVar5 = 0x103;
            goto LAB_00bb643c;
          }
          if (param_5 == '\0') {
            *(undefined2 *)((long)param_1 + 1) = 3;
            return;
          }
        }
        goto LAB_00bb63c4;
      }
      *(undefined1 *)param_1 = 3;
      *(undefined1 *)((long)param_1 + 3) = 4;
    }
    if (param_5 == '\x02') {
      uVar5 = 0x201;
LAB_00bb643c:
      *(undefined2 *)((long)param_1 + 1) = uVar5;
      if (bVar4) {
        bVar2 = *param_2;
        uVar1 = (ulong)(bVar2 >> 1);
        if ((bVar2 & 1) != 0) {
          uVar1 = *(ulong *)(param_2 + 8);
        }
        lVar7 = uVar1 - 1;
        if ((bVar2 & 1) == 0) {
          pbVar10 = param_2 + 1;
          *param_2 = (byte)((int)lVar7 << 1);
        }
        else {
          pbVar10 = *(byte **)(param_2 + 0x10);
          *(long *)(param_2 + 8) = lVar7;
        }
        pbVar10[lVar7] = 0;
        return;
      }
      return;
    }
    if (param_5 == '\x01') {
      uVar5 = 2;
LAB_00bb64bc:
      *(undefined2 *)((long)param_1 + 1) = uVar5;
                    /* try { // try from 00bb64c0 to 00cb64cb has its CatchHandler @ 00bbacac */
      if (!bVar4) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc(param_2,0x20)
        ;
        return;
      }
      return;
    }
    if (param_5 == '\0') {
      *(undefined2 *)((long)param_1 + 1) = 2;
      return;
    }
LAB_00bb63c4:
    *param_1 = (int)DAT_002b27f8;
    return;
  }
  if (param_4 != '\0') goto LAB_00bb63c4;
  if (bVar4) {
    uVar1 = *(ulong *)(param_2 + 8);
    pbVar10 = *(byte **)(param_2 + 0x10);
                    /* try { // try from 00bb605c to 00cb6063 has its CatchHandler @ 00bbae50 */
    if ((*param_2 & 1) == 0) {
      pbVar10 = param_2 + 1;
      uVar1 = (ulong)(*param_2 >> 1);
    }
                    /* try { // try from 00bb606c to 00cb607b has its CatchHandler @ 00bbadf0 */
    lVar7 = uVar1 - 3;
    if (lVar7 != 0) {
      if (uVar1 == 4) {
                    /* try { // try from 00bb6084 to 00cb608f has its CatchHandler @ 00bbadec */
        bVar2 = pbVar10[3];
        __n = (long)(pbVar10 + 3) - (long)pbVar10;
        if (__n != 0) {
          memmove(pbVar10 + (4 - __n),pbVar10,__n);
        }
        *pbVar10 = bVar2;
      }
      else if (lVar7 == 3) {
        bVar2 = *pbVar10;
        *pbVar10 = pbVar10[3];
        pbVar10[3] = bVar2;
        if (uVar1 != 4) {
                    /* try { // try from 00bb620c to 00cb620f has its CatchHandler @ 00bbacf8 */
          bVar2 = pbVar10[1];
                    /* try { // try from 00bb6210 to 00cb628f has its CatchHandler @ 00bb3444 */
          pbVar10[1] = pbVar10[4];
          pbVar10[4] = bVar2;
          if (uVar1 != 5) {
            bVar2 = pbVar10[2];
            pbVar10[2] = pbVar10[5];
            pbVar10[5] = bVar2;
          }
        }
      }
      else {
        lVar11 = 3;
        do {
          lVar6 = lVar7;
          lVar7 = 0;
          if (lVar6 != 0) {
            lVar7 = lVar11 / lVar6;
          }
          lVar7 = lVar11 - lVar7 * lVar6;
          lVar11 = lVar6;
        } while (lVar7 != 0);
        pbVar9 = pbVar10 + lVar6;
        do {
          pbVar8 = pbVar9 + -1;
          bVar2 = *pbVar8;
          pbVar12 = pbVar8;
          pbVar9 = pbVar9 + 2;
          do {
            pbVar13 = pbVar9;
            pbVar3 = pbVar13;
            if ((long)(pbVar10 + (uVar1 - (long)pbVar13)) < 4) {
              pbVar3 = pbVar10 + -(long)(pbVar10 + (uVar1 - (long)pbVar13));
            }
            *pbVar12 = *pbVar13;
            pbVar12 = pbVar13;
            pbVar9 = pbVar3 + 3;
                    /* try { // try from 00bb6290 to 00cb6297 has its CatchHandler @ 00bbacdc */
          } while (pbVar3 + 3 != pbVar8);
          *pbVar13 = bVar2;
          pbVar9 = pbVar8;
        } while (pbVar8 != pbVar10);
      }
    }
  }
  if (param_6 < 2) {
    if (param_6 == 0) {
      *param_1 = (int)DAT_002b2bf8;
      goto joined_r0x00bb61d0;
    }
    if (param_6 != 1) goto LAB_00bb63c4;
    *(undefined1 *)param_1 = 3;
    *(undefined1 *)((long)param_1 + 3) = 2;
    if (param_5 == '\x02') {
      uVar5 = 0x401;
      goto LAB_00bb64ec;
    }
    if (param_5 != '\x01') {
      if (param_5 == '\0') {
        *(undefined2 *)((long)param_1 + 1) = 4;
        return;
      }
      goto LAB_00bb63c4;
    }
    uVar5 = 4;
  }
  else {
    if (param_6 == 2) {
      *(undefined1 *)param_1 = 4;
      *(undefined1 *)((long)param_1 + 3) = 3;
      if (param_5 != '\x02') {
                    /* try { // try from 00bb634c to 00cb6357 has its CatchHandler @ 00bba79c */
        if (param_5 == '\x01') {
                    /* try { // try from 00bb63f4 to 00cb63ff has its CatchHandler @ 00bbabc0 */
          if (!bVar4) {
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmmc
                      (param_2,0,1,0x20);
                    /* try { // try from 00bb6410 to 00cb6417 has its CatchHandler @ 00bbae4c */
          }
          goto LAB_00bb6358;
        }
LAB_00bb6354:
        if (param_5 == '\0') {
LAB_00bb6358:
                    /* try { // try from 00bb6358 to 00cb6367 has its CatchHandler @ 00bba788 */
          *(undefined2 *)((long)param_1 + 1) = 0x200;
          return;
        }
        goto LAB_00bb63c4;
      }
LAB_00bb63ec:
      uVar5 = 0x102;
LAB_00bb64ec:
      *(undefined2 *)((long)param_1 + 1) = uVar5;
      if (bVar4) {
        pbVar10 = *(byte **)(param_2 + 0x10);
        if ((*param_2 & 1) == 0) {
          pbVar10 = param_2 + 1;
        }
                    /* try { // try from 00bb6524 to 00cb6533 has its CatchHandler @ 00bbad9c */
        FUN_00bb9248(param_2,pbVar10);
        return;
      }
      return;
    }
    if (param_6 == 3) {
                    /* try { // try from 00bb6368 to 00cb637b has its CatchHandler @ 00bba75c */
      *(undefined1 *)param_1 = 4;
      *(undefined1 *)((long)param_1 + 3) = 2;
      if (param_5 != '\x02') {
        if (param_5 == '\x01') {
          uVar5 = 0x301;
          goto LAB_00bb64ec;
        }
        if (param_5 == '\0') {
          *(undefined2 *)((long)param_1 + 1) = 0x300;
          return;
        }
        goto LAB_00bb63c4;
      }
      uVar5 = 3;
    }
    else {
      if (param_6 != 4) goto LAB_00bb63c4;
      *(undefined1 *)param_1 = 4;
      *(undefined1 *)((long)param_1 + 3) = 3;
      if (param_5 == '\x02') goto LAB_00bb63ec;
      if (param_5 != '\x01') goto LAB_00bb6354;
      uVar5 = 0x200;
    }
  }
  *(undefined2 *)((long)param_1 + 1) = uVar5;
joined_r0x00bb63bc:
  if (!bVar4) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmmc(param_2,0,1,0x20);
    return;
  }
  return;
}

~~~
