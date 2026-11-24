# 00aaeff0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aadffc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aad/00aadffc.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0012.md#compare-23ed69d3746be7f1e0f3122b581169b9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaeff0",
  "name": "thunk_FUN_00b341e4",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0d63fd4257e256c3775dc4e7d04a9b25488c761f74d4280497c8839479344e94",
  "source_text_sha256": "0d63fd4257e256c3775dc4e7d04a9b25488c761f74d4280497c8839479344e94",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaeff0",
        "00aaeff3"
      ]
    ],
    "bytes_sha256": "8721440e00fa03d100352c0c70e1f003bdc94909bd8c674232c30ff69e9a996f",
    "instruction_count": 1,
    "instruction_bytes": 4,
    "body_bytes": 4,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005b9f44](../005b9/005b9f44.md)
- [00796a68](../00796/00796a68.md)
- [007aac3c](../007aa/007aac3c.md)
- [007ab138](../007ab/007ab138.md)
- [00854c7c](../00854/00854c7c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2793 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void thunk_FUN_00b341e4(undefined8 param_1,undefined8 param_2)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  ulong uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  ulong uStack_c0;
  undefined8 uStack_b8;
  char *pcStack_b0;
  byte bStack_88;
  char acStack_87 [8];
  undefined7 uStack_7f;
  char cStack_78;
  undefined1 uStack_77;
  undefined6 uStack_76;
  long lStack_50;
  long lStack_48;
  
  lVar1 = tpidr_el0;
  lStack_48 = *(long *)(lVar1 + 0x28);
  uVar3 = FUN_005891cc();
  uVar4 = FUN_005894bc();
  uStack_77 = 0;
  bStack_88 = 0x20;
  uStack_7f = (undefined7)s_adjustTrackEvent_002a4cf0._8_8_;
  cStack_78 = SUB81(s_adjustTrackEvent_002a4cf0._8_8_,7);
  acStack_87[0] = s_adjustTrackEvent_002a4cf0[0];
  acStack_87[1] = s_adjustTrackEvent_002a4cf0[1];
  acStack_87[2] = s_adjustTrackEvent_002a4cf0[2];
  acStack_87[3] = s_adjustTrackEvent_002a4cf0[3];
  acStack_87[4] = s_adjustTrackEvent_002a4cf0[4];
  acStack_87[5] = s_adjustTrackEvent_002a4cf0[5];
  acStack_87[6] = s_adjustTrackEvent_002a4cf0[6];
  acStack_87[7] = s_adjustTrackEvent_002a4cf0[7];
  pcStack_b0 = (char *)_Znwm(0x28);
  uVar2 = s__Ljava_lang_String_Ljava_lang_St_002bc7b7._16_8_;
  uVar8 = s__Ljava_lang_String_Ljava_lang_St_002bc7b7._0_8_;
  uVar6 = CONCAT17(s__Ljava_lang_String_Ljava_lang_St_002bc7b7[0x1f],
                   s__Ljava_lang_String_Ljava_lang_St_002bc7b7._24_7_);
  uVar7 = CONCAT71(s__Ljava_lang_String_Ljava_lang_St_002bc7b7._32_7_,
                   s__Ljava_lang_String_Ljava_lang_St_002bc7b7[0x1f]);
  uStack_b8 = _UNK_002c23f8;
  uStack_c0 = _DAT_002c23f0;
  *(undefined8 *)(pcStack_b0 + 8) = s__Ljava_lang_String_Ljava_lang_St_002bc7b7._8_8_;
  *(undefined8 *)pcStack_b0 = uVar8;
  *(undefined8 *)(pcStack_b0 + 0x18) = uVar6;
  *(undefined8 *)(pcStack_b0 + 0x10) = uVar2;
  *(undefined8 *)(pcStack_b0 + 0x1f) = uVar7;
  pcStack_b0[0x27] = '\0';
  lStack_50 = FUN_00589680(uVar4,&bStack_88,&uStack_c0,uVar3);
  if ((uStack_c0 & 1) != 0) {
    _ZdlPv(pcStack_b0);
  }
  if ((bStack_88 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_76,CONCAT11(uStack_77,cStack_78)));
  }
  uVar5 = FUN_005894a4(&lStack_50);
  if ((uVar5 & 1) != 0) {
    FUN_00589c30(&bStack_88,uVar3,param_1);
    FUN_00589c30(&uStack_c0,uVar3,param_2);
    FUN_005894bc();
    uVar6 = FUN_00589bb0();
    uVar7 = FUN_00589bb8(&bStack_88);
    uVar8 = FUN_00589bb8(&uStack_c0);
    if (lStack_50 != 0) {
      FUN_0057504c(uVar3,uVar6,lStack_50,uVar7,uVar8);
    }
    FUN_0058ac1c(&uStack_c0);
    FUN_0058ac1c(&bStack_88);
  }
  if (*(long *)(lVar1 + 0x28) == lStack_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaeff0"></a> `00aaeff0` | `7d 14 02 14` | b 0x00b341e4 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00aaeff0`](#insn-00aaeff0) 範囲 `[['00aaeff0', '00aaeff3']]`
  - `UNCONDITIONAL_JUMP` [`00aaeff0`](#insn-00aaeff0) → [`00b341e4`](../00b34/00b341e4.md)

## 命令位置別の参照

- [`00aaeff0`](#insn-00aaeff0) → [`00b341e4`](../00b34/00b341e4.md) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `00b341e4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaeff0`](#insn-00aaeff0)

~~~json
{
  "source": "00aaeff0",
  "target": "00b341e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
