# 006deaec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "006deaec",
  "name": "FUN_006deaec",
  "size": 2736,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6e90d274e6b247b9e67a5ea45bfaefc38b6572a0a7135e0e3d69975507046338",
  "source_text_sha256": "6e90d274e6b247b9e67a5ea45bfaefc38b6572a0a7135e0e3d69975507046338"
}
~~~

## 呼び出し元

- [006b2bb4](../006b2/006b2bb4.md)
- [006f252c](../006f2/006f252c.md)

## 呼び出し先

- [0046ca04](../0046c/0046ca04.md)
- [0046d7f0](../0046d/0046d7f0.md)
- [0046ee98](../0046e/0046ee98.md)
- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [006b2744](../006b2/006b2744.md)
- [006dd2bc](../006dd/006dd2bc.md)
- [006de7e0](../006de/006de7e0.md)
- [00851550](../00851/00851550.md)
- [0085b32c](../0085b/0085b32c.md)
- [009dcf20](../009dc/009dcf20.md)

## 疑似コード / UTF-8 19197 bytes

~~~c

void FUN_006deaec(char *param_1)

{
  int iVar1;
  int iVar2;
  undefined4 uVar3;
  int iVar4;
  long lVar5;
  ulong uVar6;
  undefined8 uVar7;
  long lVar8;
  uint uVar9;
  undefined4 uVar10;
  dword *pdVar11;
  
  if (*(int *)(param_1 + 0x24) == -1) {
    return;
  }
                    /* try { // try from 006deb0c to 007deb17 has its CatchHandler @ 006dee5c */
  lVar5 = FUN_00851550();
  uVar6 = FUN_006b2744(lVar5 + 0x42ef60);
                    /* try { // try from 006deb5c to 007deb67 has its CatchHandler @ 006dee64 */
                    /* try { // try from 006deb68 to 007debb7 has its CatchHandler @ 006de6c0 */
  if ((((((uVar6 & 1) != 0) &&
        (lVar5 = FUN_00851550(), *(int *)(BYTE_ARRAY_0042ef8d + lVar5 + 0x23) != 2)) &&
       (uVar6 = FUN_006de7e0(param_1), (uVar6 & 1) != 0)) &&
      (lVar5 = FUN_00851550(), *(int *)((long)&DWORD_004326e0 + lVar5) == -1)) &&
     ((((lVar5 = FUN_00851550(), *(char *)((long)&DWORD_004316b4 + lVar5) != '\0' &&
        (lVar5 = FUN_00851550(), BYTE_ARRAY_00431665[lVar5 + 0x1b] == 0)) ||
       (lVar5 = FUN_00851550(), (*(byte *)((long)&DWORD_004316b4 + lVar5) & 1) == 0)) &&
      (lVar5 = FUN_00851550(), *(int *)((long)&DWORD_0042efc0 + lVar5) == 0)))) {
    lVar5 = FUN_00851550();
                    /* try { // try from 006debb8 to 007debe3 has its CatchHandler @ 006dee78 */
    uVar6 = FUN_006dd2bc(lVar5 + 0x42f7b0);
    if ((((uVar6 & 1) == 0) && (lVar5 = FUN_00851550(), *(int *)(&uleb128_0042efc4 + lVar5) == 0))
       && (lVar5 = FUN_00851550(), *(int *)(BYTE_ARRAY_0042efcd + lVar5 + 3) == 0)) {
      lVar5 = FUN_00851550();
      uVar3 = *(undefined4 *)(param_1 + 0x24);
      *(int *)(&uleb128_0042efc4 + lVar5) = *(int *)(&uleb128_0042efc4 + lVar5) + 1;
      lVar5 = FUN_00851550();
      *(undefined4 *)((long)&QWORD_0042efc5 + lVar5 + 3) = uVar3;
      uVar7 = FUN_0047ad34();
      FUN_0047ce14(uVar7,0xb,0);
    }
  }
  FUN_00851550();
  uVar6 = FUN_0085b32c();
  if ((uVar6 & 1) != 0) {
    uVar7 = FUN_00851550();
                    /* try { // try from 006dec64 to 007dec6b has its CatchHandler @ 006dee64 */
    uVar6 = FUN_009dcf20(uVar7,*(int *)(param_1 + 4) / 100 + -0x3c,
                         *(int *)(param_1 + 8) / 100 + -0x78,0x78,0x78);
    if (((uVar6 & 1) != 0) &&
       (lVar5 = FUN_00851550(), *(int *)((long)&QWORD_0042efc5 + lVar5 + 7) == -1)) {
                    /* try { // try from 006dec90 to 007dec9b has its CatchHandler @ 006dee58 */
      lVar5 = FUN_00851550();
      uVar6 = FUN_006b2744(lVar5 + 0x42ef60);
                    /* try { // try from 006decdc to 007ded1f has its CatchHandler @ 006dee60 */
      if (((uVar6 & 1) != 0) &&
         (((lVar5 = FUN_00851550(), *(int *)((long)&DWORD_004326e0 + lVar5) == -1 &&
           (lVar5 = FUN_00851550(), (BYTE_ARRAY_00431665[lVar5 + 0x1b] & 1) == 0)) &&
          (lVar5 = FUN_00851550(), *(int *)((long)&DWORD_0042efc0 + lVar5) == 0)))) {
        lVar5 = FUN_00851550();
        uVar6 = FUN_006dd2bc(lVar5 + 0x42f7b0);
        if ((((uVar6 & 1) == 0) &&
            (lVar5 = FUN_00851550(), *(int *)(&uleb128_0042efc4 + lVar5) == 0)) &&
           (lVar5 = FUN_00851550(), *(int *)(BYTE_ARRAY_0042efcd + lVar5 + 3) == 0)) {
          uVar3 = *(undefined4 *)(param_1 + 0x24);
          lVar5 = FUN_00851550();
          *(undefined4 *)((long)&QWORD_0042efc5 + lVar5 + 7) = uVar3;
          uVar7 = FUN_0047ad34();
          FUN_0047ce14(uVar7,10,0);
        }
      }
    }
  }
  lVar5 = FUN_00851550();
                    /* try { // try from 006ded50 to 007ded5b has its CatchHandler @ 006dee54 */
  if (*(char *)((long)&QWORD_004326e5 + lVar5 + 4) != '\0') {
    iVar1 = *(int *)(param_1 + 0x44);
    *(int *)(param_1 + 0x44) = iVar1 + 1;
    if (0x382 < iVar1) {
      lVar5 = FUN_00851550();
      *(undefined1 *)((long)&QWORD_004326e5 + lVar5 + 4) = 0;
    }
    *param_1 = '\0';
    if (*(int *)(param_1 + 0x38) != 0) {
      lVar5 = FUN_00851550();
      param_1[0xc] = '\0';
      param_1[0xd] = '\0';
      param_1[0xe] = '\0';
      param_1[0xf] = '\0';
                    /* try { // try from 006ded98 to 007dedbf has its CatchHandler @ 006dee50 */
      *(undefined1 *)((long)&QWORD_004326e5 + lVar5 + 4) = 0;
    }
    iVar1 = *(int *)(param_1 + 0x30);
    iVar2 = *(int *)(param_1 + 4);
    *(int *)(param_1 + 0x1c) = *(int *)(param_1 + 0x1c) + 1;
    if (iVar1 < iVar2) {
      *(int *)(param_1 + 4) = iVar2 + -1000;
      param_1[0x20] = '\x03';
      param_1[0x21] = '\0';
      param_1[0x22] = '\0';
      param_1[0x23] = '\0';
      if (iVar1 < iVar2 + -1000) goto LAB_006dee1c;
    }
    else {
                    /* try { // try from 006dedfc to 007dee1b has its CatchHandler @ 006dee80 */
      if (iVar1 <= iVar2) {
        lVar5 = FUN_00851550();
                    /* catch() { ... } // from try @ 006ded98 with catch @ 006dee50
                       try { // try from 006dee50 to 007deebf has its CatchHandler @ 006de6c0 */
                    /* catch() { ... } // from try @ 006ded50 with catch @ 006dee54 */
                    /* catch() { ... } // from try @ 006dec90 with catch @ 006dee58 */
                    /* catch() { ... } // from try @ 006deb0c with catch @ 006dee5c */
                    /* catch() { ... } // from try @ 006decdc with catch @ 006dee60 */
        if (*(char *)((long)&QWORD_004326e5 + lVar5 + 5) == '\0') {
          if (*(int *)(param_1 + 0x20) - 3U < 2) {
            lVar5 = 0x14;
            pdVar11 = &fde_0042fcc4;
            param_1[0x20] = '\a';
            param_1[0x21] = '\0';
            param_1[0x22] = '\0';
            param_1[0x23] = '\0';
            do {
                    /* catch() { ... } // from try @ 006def14 with catch @ 006df0d0 */
              FUN_00851550();
                    /* catch() { ... } // from try @ 006df044 with catch @ 006df0d4 */
              lVar8 = FUN_00851550();
              if ((*(int *)(lVar8 + (long)pdVar11) != -1) &&
                 (lVar8 = FUN_00851550(), *(int *)((long)pdVar11 + lVar8 + -4) != 7))
              goto LAB_006df2f0;
              FUN_00851550();
              lVar5 = lVar5 + -1;
                    /* catch() { ... } // from try @ 006defd8 with catch @ 006df0c8 */
              pdVar11 = pdVar11 + 0x12;
                    /* catch() { ... } // from try @ 006def80 with catch @ 006df0cc */
            } while (lVar5 != 0);
            lVar5 = FUN_00851550();
            if ((((*(int *)(BYTE_ARRAY_00434675 + lVar5 + 0xb) == -1) ||
                 (lVar5 = FUN_00851550(), *(int *)((long)&DWORD_00430260 + lVar5) == 7)) ||
                (lVar5 = FUN_00851550(), *(int *)(BYTE_ARRAY_004362f5 + lVar5 + 7) == 0)) ||
               (lVar5 = FUN_00851550(), *(int *)(BYTE_ARRAY_004305e1 + lVar5 + 7) == 7)) {
              lVar5 = FUN_00851550();
              *(undefined1 *)((long)&QWORD_004326e5 + lVar5 + 5) = 1;
            }
            FUN_00851550();
          }
LAB_006df2f0:
          param_1[0x20] = '\a';
          param_1[0x21] = '\0';
          param_1[0x22] = '\0';
          param_1[0x23] = '\0';
        }
        else {
                    /* catch() { ... } // from try @ 006deb5c with catch @ 006dee64
                       catch() { ... } // from try @ 006dec64 with catch @ 006dee64 */
                    /* catch() { ... } // from try @ 006de828 with catch @ 006dee68 */
          if (*(int *)(param_1 + 0x20) == 7) {
                    /* catch() { ... } // from try @ 006deab0 with catch @ 006dee6c */
            param_1[0x1c] = '\0';
            param_1[0x1d] = '\0';
            param_1[0x1e] = '\0';
            param_1[0x1f] = '\0';
            param_1[0x20] = '\0';
            param_1[0x21] = '\0';
            param_1[0x22] = '\0';
            param_1[0x23] = '\0';
                    /* catch() { ... } // from try @ 006de7cc with catch @ 006dee70 */
          }
          else if (0x19 < *(int *)(param_1 + 0x1c)) {
            lVar5 = FUN_00851550();
            param_1[0x20] = '\a';
            param_1[0x21] = '\0';
            param_1[0x22] = '\0';
            param_1[0x23] = '\0';
            *(undefined1 *)((long)&QWORD_004326e5 + lVar5 + 5) = 0;
            lVar5 = FUN_00851550();
            FUN_0046ee98((long)&DWORD_0042f460 + lVar5 + (ulong)*(uint *)(param_1 + 0x20) * 0x38);
            uVar3 = FUN_0046d7f0();
            *(undefined4 *)(param_1 + 0x1c) = uVar3;
          }
        }
        goto LAB_006dee1c;
      }
      *(int *)(param_1 + 4) = iVar2 + 1000;
      param_1[0x20] = '\x04';
      param_1[0x21] = '\0';
      param_1[0x22] = '\0';
      param_1[0x23] = '\0';
      if (iVar2 + 1000 < iVar1) goto LAB_006dee1c;
    }
    *(int *)(param_1 + 4) = iVar1;
LAB_006dee1c:
    lVar5 = FUN_00851550();
                    /* try { // try from 006dee30 to 007dee4f has its CatchHandler @ 006dee7c */
    iVar1 = FUN_0046ee98((long)&DWORD_0042f460 + lVar5 + (ulong)*(uint *)(param_1 + 0x20) * 0x38);
    if (*(int *)(param_1 + 0x1c) < iVar1 * 4) {
      return;
    }
    param_1[0x1c] = '\0';
    param_1[0x1d] = '\0';
    param_1[0x1e] = '\0';
    param_1[0x1f] = '\0';
    return;
  }
  if (*param_1 != '\0') {
    if (*(int *)(param_1 + 0x38) == 0) {
      iVar1 = *(int *)(param_1 + 0x1c);
      *(int *)(param_1 + 0x1c) = iVar1 + 1;
      if (*(int *)(param_1 + 0x20) == 2) {
        if (iVar1 < 0x77) {
          return;
        }
        *param_1 = '\0';
        return;
      }
      if (*(int *)(param_1 + 0x20) != 4) {
        return;
      }
      iVar2 = *(int *)(param_1 + 4);
      *(int *)(param_1 + 4) = iVar2 + 1000;
                    /* try { // try from 006df044 to 007df06b has its CatchHandler @ 006df0d4 */
      FUN_00851550();
      iVar1 = FUN_0046ca04();
      if (iVar1 < 0) {
        iVar1 = iVar1 + 1;
      }
      if ((iVar2 + 1000) / 100 < (iVar1 >> 1) + -0xb4) {
        return;
      }
      FUN_00851550();
                    /* try { // try from 006df06c to 007df103 has its CatchHandler @ 006deec0 */
      iVar1 = FUN_0046ca04();
      uVar7 = DAT_002c40c0;
      if (iVar1 < 0) {
        iVar1 = iVar1 + 1;
      }
      *(int *)(param_1 + 4) = (iVar1 >> 1) * 100 + -18000;
      *(undefined8 *)(param_1 + 0x1c) = uVar7;
      return;
    }
    *param_1 = '\0';
    param_1[0x20] = '\b';
    param_1[0x21] = '\0';
    param_1[0x22] = '\0';
    param_1[0x23] = '\0';
    iVar1 = *(int *)(param_1 + 0x1c) + 1;
LAB_006df41c:
    *(int *)(param_1 + 0x1c) = iVar1;
    return;
  }
                    /* catch() { ... } // from try @ 006de75c with catch @ 006dee74 */
  lVar5 = FUN_00851550();
                    /* catch() { ... } // from try @ 006debb8 with catch @ 006dee78 */
                    /* catch() { ... } // from try @ 006dee30 with catch @ 006dee7c */
                    /* catch() { ... } // from try @ 006dedfc with catch @ 006dee80 */
                    /* catch() { ... } // from try @ 006de9a8 with catch @ 006dee84 */
  if (*(int *)(BYTE_ARRAY_0042ef8d + lVar5 + 0x23) != 0) {
                    /* catch() { ... } // from try @ 006de894 with catch @ 006dee88 */
    iVar1 = *(int *)(param_1 + 0x38);
                    /* catch() { ... } // from try @ 006de904 with catch @ 006dee8c */
    if ((iVar1 != 0) && (*(int *)(param_1 + 0x38) = iVar1 + -1, iVar1 + -1 == 0 || iVar1 < 1)) {
      param_1[0x38] = '\0';
      param_1[0x39] = '\0';
      param_1[0x3a] = '\0';
      param_1[0x3b] = '\0';
      iVar1 = FUN_0046d7f0(0x18);
      param_1[0x20] = '\x03';
      param_1[0x21] = '\0';
      param_1[0x22] = '\0';
      param_1[0x23] = '\0';
      *(int *)(param_1 + 0xc) = iVar1 * -10 + -0x35c;
    }
                    /* catch() { ... } // from try @ 006deffc with catch @ 006deec0
                       catch() { ... } // from try @ 006df06c with catch @ 006deec0 */
    iVar1 = *(int *)(param_1 + 0x3c);
    if ((iVar1 != 0) && (*(int *)(param_1 + 0x3c) = iVar1 + -1, iVar1 + -1 == 0 || iVar1 < 1)) {
      param_1[0x3c] = '\0';
      param_1[0x3d] = '\0';
      param_1[0x3e] = '\0';
      param_1[0x3f] = '\0';
      iVar1 = FUN_0046d7f0(0xc);
      param_1[0x20] = '\x04';
      param_1[0x21] = '\0';
      param_1[0x22] = '\0';
      param_1[0x23] = '\0';
      *(int *)(param_1 + 0xc) = iVar1 * 0x14 + 0x35c;
      FUN_00851550();
      iVar1 = FUN_0046ca04();
      if (iVar1 < 0) {
        iVar1 = iVar1 + 1;
      }
      iVar2 = FUN_0046d7f0(0xf0);
                    /* try { // try from 006def14 to 007def1f has its CatchHandler @ 006df0d0 */
      *(int *)(param_1 + 0x40) = ((iVar1 >> 1) - iVar2) + -0x50;
      FUN_00851550();
      iVar1 = FUN_0046ca04();
      if (iVar1 < 0) {
        iVar1 = iVar1 + 1;
      }
      *(int *)(param_1 + 4) = (*(int *)(param_1 + 0x40) - (iVar1 >> 1)) * 100 + -10000;
    }
    iVar1 = *(int *)(param_1 + 0x40);
    if ((iVar1 != 0) && (iVar1 <= *(int *)(param_1 + 4) / 100)) {
      param_1[0xc] = '\0';
      param_1[0xd] = '\0';
      param_1[0xe] = '\0';
      param_1[0xf] = '\0';
                    /* try { // try from 006def80 to 007defa3 has its CatchHandler @ 006df0cc */
      param_1[0x40] = '\0';
      param_1[0x41] = '\0';
      param_1[0x42] = '\0';
      param_1[0x43] = '\0';
      param_1[0x20] = '\b';
      param_1[0x21] = '\0';
      param_1[0x22] = '\0';
      param_1[0x23] = '\0';
      *(int *)(param_1 + 4) = iVar1 * 100;
      lVar5 = FUN_00851550();
      FUN_0046ee98((long)&DWORD_0042f460 + lVar5 + (ulong)*(uint *)(param_1 + 0x20) * 0x38);
      uVar3 = FUN_0046d7f0();
      *(undefined4 *)(param_1 + 0x1c) = uVar3;
    }
    iVar1 = *(int *)(param_1 + 0x20);
    if (iVar1 == 8) {
      lVar5 = FUN_00851550();
                    /* try { // try from 006defd8 to 007deffb has its CatchHandler @ 006df0c8 */
      if ((*(int *)((long)&DWORD_0042f7d4 + lVar5) == 5) ||
         (lVar5 = FUN_00851550(), *(int *)((long)&DWORD_0042f7d4 + lVar5) == 6)) {
        lVar5 = FUN_00851550();
                    /* try { // try from 006deffc to 007df043 has its CatchHandler @ 006deec0 */
        iVar1 = *(int *)((long)&DWORD_0042f7d4 + lVar5);
        *(int *)(param_1 + 0x20) = iVar1;
      }
      else {
        iVar1 = *(int *)(param_1 + 0x20);
      }
    }
    if ((iVar1 - 5U < 2) &&
       (lVar5 = FUN_00851550(), iVar1 != *(int *)((long)&DWORD_0042f7d4 + lVar5))) {
      lVar5 = FUN_00851550();
      *(undefined4 *)(param_1 + 0x20) = *(undefined4 *)((long)&DWORD_0042f7d4 + lVar5);
      uVar3 = FUN_0046d7f0(10);
      *(undefined4 *)(param_1 + 0x1c) = uVar3;
    }
    *(int *)(param_1 + 4) = *(int *)(param_1 + 4) + *(int *)(param_1 + 0xc);
    lVar5 = FUN_00851550();
    iVar2 = FUN_0046ee98((long)&DWORD_0042f460 + lVar5 + (ulong)*(uint *)(param_1 + 0x20) * 0x38);
    iVar1 = 0;
    if (*(int *)(param_1 + 0x1c) + 1 < iVar2) {
      iVar1 = *(int *)(param_1 + 0x1c) + 1;
    }
    goto LAB_006df41c;
  }
  uVar9 = *(int *)(param_1 + 4) + *(int *)(param_1 + 0xc);
  *(uint *)(param_1 + 4) = uVar9;
  if ((int)uVar9 < 8000) {
    iVar1 = 8000;
    uVar3 = 7;
LAB_006df1bc:
    *(int *)(param_1 + 4) = iVar1;
    *(undefined4 *)(param_1 + 0x20) = uVar3;
    param_1[0xc] = '\0';
    param_1[0xd] = '\0';
    param_1[0xe] = '\0';
    param_1[0xf] = '\0';
    lVar5 = FUN_00851550();
    FUN_0046ee98((long)&DWORD_0042f460 + lVar5 + (ulong)*(uint *)(param_1 + 0x20) * 0x38);
    uVar3 = FUN_0046d7f0();
    *(undefined4 *)(param_1 + 0x1c) = uVar3;
  }
  else {
    FUN_00851550();
    iVar1 = FUN_0046ca04();
    if (iVar1 + -0x50 < (int)(uVar9 / 100)) {
      FUN_00851550();
      iVar1 = FUN_0046ca04();
      iVar1 = iVar1 * 100 + -8000;
      uVar3 = 8;
      goto LAB_006df1bc;
    }
  }
  lVar5 = FUN_00851550();
  iVar4 = FUN_0046ee98((long)&DWORD_0042f460 + lVar5 + (ulong)*(uint *)(param_1 + 0x20) * 0x38);
  iVar2 = *(int *)(param_1 + 0x1c);
  *(int *)(param_1 + 0x1c) = iVar2 + 1;
  iVar1 = iVar4 << 2;
  if (1 < *(int *)(param_1 + 0x20) - 7U) {
    iVar1 = iVar4;
  }
  if (iVar2 + 1 < iVar1) {
    return;
  }
  param_1[0x1c] = '\0';
  param_1[0x1d] = '\0';
  param_1[0x1e] = '\0';
  param_1[0x1f] = '\0';
  iVar1 = FUN_0046d7f0(3);
  if (iVar1 < 2) {
    if (iVar1 != 0) {
      if (iVar1 != 1) {
        return;
      }
      param_1[0x20] = '\t';
      param_1[0x21] = '\0';
      param_1[0x22] = '\0';
      param_1[0x23] = '\0';
      param_1[0xc] = -0x2c;
      param_1[0xd] = -2;
      param_1[0xe] = -1;
      param_1[0xf] = -1;
      if (0x1fa3 < *(int *)(param_1 + 4)) {
        return;
      }
      iVar1 = 8000;
      uVar3 = 7;
      param_1[0xc] = '\0';
      param_1[0xd] = '\0';
      param_1[0xe] = '\0';
      param_1[0xf] = '\0';
LAB_006df524:
      *(int *)(param_1 + 4) = iVar1;
      *(undefined4 *)(param_1 + 0x20) = uVar3;
      return;
    }
    iVar2 = *(int *)(param_1 + 4);
    FUN_00851550();
    iVar1 = FUN_0046ca04();
    if (iVar1 < 0) {
      iVar1 = iVar1 + 1;
    }
    if ((iVar1 >> 1) + -0x5a <= iVar2 / 100) {
      iVar2 = *(int *)(param_1 + 4);
      FUN_00851550();
      iVar1 = FUN_0046ca04();
      if (iVar1 < 0) {
        iVar1 = iVar1 + 1;
      }
      if (iVar2 / 100 <= (iVar1 >> 1) + 0x5a) {
LAB_006df530:
        if (*(int *)(param_1 + 0xc) < 0) {
          uVar3 = 0xfffffed4;
          uVar10 = 9;
        }
        else {
          uVar3 = 300;
          uVar10 = 10;
        }
        *(undefined4 *)(param_1 + 0xc) = uVar3;
        *(undefined4 *)(param_1 + 0x20) = uVar10;
        return;
      }
    }
    if (*(int *)(param_1 + 0xc) == 0) {
      if (*(int *)(param_1 + 0x20) == 0) {
        uVar9 = 7;
      }
      else {
        if (*(int *)(param_1 + 0x20) != 1) goto LAB_006df4c0;
        uVar9 = 8;
      }
    }
    else {
      uVar9 = 7;
      if (-1 < *(int *)(param_1 + 0xc)) {
        uVar9 = 8;
      }
    }
  }
  else {
    if (iVar1 == 2) {
      iVar1 = *(int *)(param_1 + 4);
      param_1[0x20] = '\n';
      param_1[0x21] = '\0';
      param_1[0x22] = '\0';
      param_1[0x23] = '\0';
      param_1[0xc] = ',';
      param_1[0xd] = '\x01';
      param_1[0xe] = '\0';
      param_1[0xf] = '\0';
      FUN_00851550();
      iVar2 = FUN_0046ca04();
      if (iVar1 / 100 < iVar2 + -0x50) {
        return;
      }
      FUN_00851550();
      iVar1 = FUN_0046ca04();
      param_1[0xc] = '\0';
      param_1[0xd] = '\0';
      param_1[0xe] = '\0';
      param_1[0xf] = '\0';
      iVar1 = iVar1 * 100 + -8000;
      uVar3 = 8;
      goto LAB_006df524;
    }
    if (iVar1 != 3) {
      return;
    }
    iVar2 = *(int *)(param_1 + 4);
    FUN_00851550();
    iVar1 = FUN_0046ca04();
    if (iVar1 < 0) {
      iVar1 = iVar1 + 1;
    }
    if ((iVar1 >> 1) + -0x5a <= iVar2 / 100) {
      iVar2 = *(int *)(param_1 + 4);
      FUN_00851550();
      iVar1 = FUN_0046ca04();
      if (iVar1 < 0) {
        iVar1 = iVar1 + 1;
      }
      if (iVar2 / 100 <= (iVar1 >> 1) + 0x5a) goto LAB_006df530;
    }
    if (*(uint *)(param_1 + 0xc) == 0) {
      if (*(int *)(param_1 + 0x20) == 7) {
        uVar9 = 0;
      }
      else {
        if (*(int *)(param_1 + 0x20) != 8) goto LAB_006df4c0;
        uVar9 = 1;
      }
    }
    else {
      uVar9 = ~*(uint *)(param_1 + 0xc) >> 0x1f;
    }
  }
  *(uint *)(param_1 + 0x20) = uVar9;
LAB_006df4c0:
  param_1[0xc] = '\0';
  param_1[0xd] = '\0';
  param_1[0xe] = '\0';
  param_1[0xf] = '\0';
  return;
}

~~~
