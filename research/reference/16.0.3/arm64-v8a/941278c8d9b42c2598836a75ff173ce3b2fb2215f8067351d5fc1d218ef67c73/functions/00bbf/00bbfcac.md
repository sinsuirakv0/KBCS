# 00bbfcac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bbfcac",
  "name": "_ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers16VerifierTemplateILb0EEE",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "529b51bf3ac21a15738c6b006117b628cc8fa2ab478770ca310ea79577b8629d",
  "source_text_sha256": "529b51bf3ac21a15738c6b006117b628cc8fa2ab478770ca310ea79577b8629d"
}
~~~

## 呼び出し元

- [00c5e570](../00c5e/00c5e570.md)

## 呼び出し先

- [00c5e580](../00c5e/00c5e580.md)
- [00c5e5a0](../00c5e/00c5e5a0.md)
- [00c5e5b0](../00c5e/00c5e5b0.md)
- [00c5e5c0](../00c5e/00c5e5c0.md)

## 疑似コード / UTF-8 4399 bytes

~~~c

undefined4
_ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
          (int *param_1,long *param_2)

{
  uint uVar1;
  uint uVar2;
  uint *puVar3;
  ushort uVar4;
  int iVar5;
  long lVar6;
  ulong uVar7;
  ulong uVar8;
  ulong uVar9;
  ulong uVar10;
  ushort *puVar11;
  
  lVar6 = *param_2;
  uVar8 = (long)param_1 - lVar6;
                    /* try { // try from 00bbfcd0 to 00cbfceb has its CatchHandler @ 00bc0414 */
  if (((uVar8 & 3) == 0) || ((char)param_2[3] == '\0')) {
    uVar7 = param_2[1];
    if (uVar7 < 5) {
      return 0;
    }
    uVar9 = uVar7 - 4;
                    /* try { // try from 00bbfcec to 00cbfd97 has its CatchHandler @ 00bbf85c */
    if (uVar9 < uVar8) {
      return 0;
    }
    iVar5 = *param_1;
    uVar1 = (int)param_2[7] + 1;
    uVar2 = *(int *)((long)param_2 + 0x3c) + 1;
    *(uint *)(param_2 + 7) = uVar1;
    *(uint *)((long)param_2 + 0x3c) = uVar2;
    if ((((uVar1 <= *(uint *)(param_2 + 2)) && (uVar2 <= *(uint *)((long)param_2 + 0x14))) &&
        ((uVar10 = uVar8 - (long)iVar5, (uVar10 & 1) == 0 || ((char)param_2[3] == '\0')))) &&
       (uVar10 <= uVar7 - 2)) {
      uVar4 = *(ushort *)(lVar6 + uVar10);
      if ((((uVar4 & 1) == 0) || ((char)param_2[3] == '\0')) && ((uVar4 & 1) == 0)) {
        if (uVar7 <= uVar4) {
          return 0;
        }
        if (uVar7 - uVar4 < uVar10) {
          return 0;
        }
        puVar11 = (ushort *)((long)param_1 - (long)*param_1);
        if (4 < *puVar11) {
          if (((ulong)puVar11[2] != 0) && (uVar7 - 1 < uVar8 + puVar11[2])) {
            return 0;
          }
          if (*puVar11 < 7) {
            lVar6 = 0;
            uVar4 = puVar11[2];
          }
          else {
            if ((ulong)puVar11[3] != 0) {
              uVar8 = uVar8 + puVar11[3];
                    /* try { // try from 00bbfdb4 to 00cc0157 has its CatchHandler @ 00bbf85c */
              if ((uVar8 & 3) == 0) {
                if (uVar9 < uVar8) {
                  return 0;
                }
              }
              else {
                if ((char)param_2[3] != '\0') {
                  return 0;
                }
                if (uVar9 < uVar8) {
                  return 0;
                }
              }
              if ((int)*(uint *)(lVar6 + uVar8) < 1) {
                return 0;
              }
              if (uVar7 - 1 < uVar8 + *(uint *)(lVar6 + uVar8)) {
                return 0;
              }
            }
            lVar6 = 0;
            if ((ulong)puVar11[3] != 0) {
              puVar3 = (uint *)((long)param_1 + (ulong)puVar11[3]);
              lVar6 = (long)puVar3 + (ulong)*puVar3;
            }
            uVar4 = puVar11[2];
          }
          if ((ulong)uVar4 != 0) {
            switch(*(undefined1 *)((long)param_1 + (ulong)uVar4)) {
            case 1:
              if (lVar6 == 0) goto switchD_00bbfe48_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp17SerializedMessage6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 2:
              if (lVar6 == 0) goto switchD_00bbfe48_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp23SerializedTokenReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 3:
              if (lVar6 == 0) goto switchD_00bbfe48_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp30SerializedRegistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            case 4:
              if (lVar6 == 0) goto switchD_00bbfe48_default;
              uVar8 = _ZNK3com6google8firebase9messaging3cpp32SerializedUnregistrationReceived6VerifyERN11flatbuffers16VerifierTemplateILb0EEE
                                (lVar6,param_2);
              break;
            default:
              goto switchD_00bbfe48_default;
            }
            if ((uVar8 & 1) == 0) {
              return 0;
            }
          }
        }
switchD_00bbfe48_default:
        *(int *)(param_2 + 7) = (int)param_2[7] + -1;
        return 1;
      }
    }
  }
                    /* try { // try from 00bbfd98 to 00cbfdb3 has its CatchHandler @ 00bc041c */
  return 0;
}

~~~
