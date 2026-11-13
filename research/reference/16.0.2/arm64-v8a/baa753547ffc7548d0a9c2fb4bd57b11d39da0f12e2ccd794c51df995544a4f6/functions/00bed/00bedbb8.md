# 00bedbb8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bedbb8",
  "name": "FUN_00bedbb8",
  "size": 672,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fde264796bd08401ddd50d154cff0c3089f2bd109fc6964ea19fc7be43088ec0",
  "source_text_sha256": "fde264796bd08401ddd50d154cff0c3089f2bd109fc6964ea19fc7be43088ec0"
}
~~~

## 呼び出し元

- [00be71ac](../00be7/00be71ac.md)

## 呼び出し先

- [00bede58](../00bed/00bede58.md)

## 疑似コード / UTF-8 4555 bytes

~~~c

bool FUN_00bedbb8(ulong *param_1,ulong *param_2)

{
  long lVar1;
  ulong uVar2;
  ulong uVar3;
  int iVar4;
  ulong uVar5;
  ulong *puVar6;
  long lVar7;
  ulong uVar8;
  ulong *puVar9;
  ulong *puVar10;
  ulong uVar11;
  long lVar12;
  ulong *puVar13;
  
  uVar3 = (long)param_2 - (long)param_1 >> 3;
  if (2 < (long)uVar3) {
    if (uVar3 == 3) {
      uVar3 = *param_1;
      uVar5 = param_1[1];
      uVar11 = param_2[-1];
      if (uVar3 <= uVar5) {
        if (uVar5 <= uVar11) {
          return true;
        }
        param_1[1] = uVar11;
        param_2[-1] = uVar5;
        uVar3 = *param_1;
        if (param_1[1] < uVar3) {
          *param_1 = param_1[1];
          param_1[1] = uVar3;
          return true;
        }
        return true;
      }
      if (uVar11 < uVar5) {
        *param_1 = uVar11;
      }
      else {
        *param_1 = uVar5;
        param_1[1] = uVar3;
        if (uVar3 <= param_2[-1]) {
          return true;
        }
        param_1[1] = param_2[-1];
      }
      goto LAB_00bede2c;
    }
    if (uVar3 != 4) {
      if (uVar3 == 5) {
        FUN_00bede58(param_1,param_1 + 1,param_1 + 2,param_1 + 3,param_2 + -1);
        return true;
      }
      goto LAB_00bedc48;
    }
    uVar5 = *param_1;
    puVar10 = param_1 + 1;
    uVar3 = *puVar10;
    puVar6 = param_1 + 2;
    uVar11 = *puVar6;
    puVar9 = param_1;
    if (uVar3 < uVar5) {
      uVar2 = uVar5;
      puVar13 = puVar6;
                    /* try { // try from 00bedcb4 to 00cedcbb has its CatchHandler @ 00bedd0c */
      if (uVar3 <= uVar11) {
                    /* try { // try from 00bedcbc to 00ceddff has its CatchHandler @ 00bed9ec */
        *param_1 = uVar3;
        param_1[1] = uVar5;
        uVar3 = uVar11;
        puVar9 = puVar10;
        goto joined_r0x00beddc4;
      }
    }
    else {
      uVar8 = uVar11;
      if (uVar3 <= uVar11) goto LAB_00bedddc;
      *puVar10 = uVar11;
      *puVar6 = uVar3;
      puVar13 = puVar10;
      uVar2 = uVar3;
joined_r0x00beddc4:
      uVar8 = uVar3;
      if (uVar5 <= uVar11) goto LAB_00bedddc;
    }
    *puVar9 = uVar11;
    *puVar13 = uVar5;
    uVar8 = uVar2;
LAB_00bedddc:
                    /* catch() { ... } // from try @ 00beda9c with catch @ 00bedde0 */
    if (uVar8 <= param_2[-1]) {
      return true;
    }
    *puVar6 = param_2[-1];
    param_2[-1] = uVar8;
    uVar5 = *puVar6;
    uVar3 = *puVar10;
    if (uVar5 < uVar3) {
      uVar11 = *param_1;
      param_1[1] = uVar5;
      param_1[2] = uVar3;
      if (uVar5 < uVar11) {
        *param_1 = uVar5;
        param_1[1] = uVar11;
        return true;
      }
      return true;
    }
    return true;
  }
  if (uVar3 < 2) {
    return true;
  }
  if (uVar3 == 2) {
    uVar3 = *param_1;
    if (uVar3 <= param_2[-1]) {
      return true;
    }
    *param_1 = param_2[-1];
LAB_00bede2c:
    param_2[-1] = uVar3;
    return true;
  }
LAB_00bedc48:
  uVar3 = *param_1;
  puVar6 = param_1 + 1;
  uVar11 = *puVar6;
  puVar10 = param_1 + 2;
  uVar5 = *puVar10;
  puVar9 = param_1;
  if (uVar11 < uVar3) {
    puVar13 = puVar10;
    if (uVar11 <= uVar5) {
      *param_1 = uVar11;
      param_1[1] = uVar3;
      puVar9 = puVar6;
      goto joined_r0x00bedd18;
    }
  }
  else {
    if (uVar11 <= uVar5) goto LAB_00bedd24;
                    /* catch() { ... } // from try @ 00bedcb4 with catch @ 00bedd0c */
    *puVar6 = uVar5;
    *puVar10 = uVar11;
    puVar13 = puVar6;
joined_r0x00bedd18:
    if (uVar3 <= uVar5) goto LAB_00bedd24;
  }
  *puVar9 = uVar5;
  *puVar13 = uVar3;
LAB_00bedd24:
  if (param_1 + 3 != param_2) {
    iVar4 = 0;
    lVar7 = 0x18;
    puVar9 = param_1 + 3;
    do {
      puVar6 = puVar9;
      uVar5 = *puVar6;
      uVar3 = *puVar10;
      lVar12 = lVar7;
      if (uVar5 < uVar3) {
        do {
          lVar1 = lVar12 + -8;
          *(ulong *)((long)param_1 + lVar12) = uVar3;
          puVar9 = param_1;
          if (lVar1 == 0) goto LAB_00bedd40;
          uVar3 = *(ulong *)((long)param_1 + lVar12 + -0x10);
          lVar12 = lVar1;
        } while (uVar5 < uVar3);
        puVar9 = (ulong *)((long)param_1 + lVar1);
LAB_00bedd40:
        iVar4 = iVar4 + 1;
                    /* catch() { ... } // from try @ 00beda90 with catch @ 00bedd44 */
        *puVar9 = uVar5;
        if (iVar4 == 8) {
          return puVar6 + 1 == param_2;
        }
      }
                    /* catch() { ... } // from try @ 00bedad8 with catch @ 00bedd54 */
      lVar7 = lVar7 + 8;
      puVar9 = puVar6 + 1;
      puVar10 = puVar6;
    } while (puVar6 + 1 != param_2);
  }
  return true;
}

~~~
