# 00c2aebc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c2aa94`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2aa94.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0008.md#compare-f93dd374b65f744ec78b21fd7b5a433a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c2af58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2a/00c2af58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/detail_skipped-0009.md#compare-81afe40dfa81dc6660836cb53d2e6e05)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c2aebc",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6bfbecd6a714d8d78fe954ecc17786f7620c273afe369330f8a1c6d32bcd7297",
  "source_text_sha256": "6bfbecd6a714d8d78fe954ecc17786f7620c273afe369330f8a1c6d32bcd7297",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c2aebc",
        "00c2af57"
      ]
    ],
    "bytes_sha256": "34db149ac8c9e5807d1f9f475b21ac4ed7ea577172a477f92c56e3f59880f228",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1370 bytes

~~~c

undefined8
_ZNKSt6__ndk115__codecvt_utf16IDsLb1EE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_
          (long param_1,undefined8 param_2,ushort *param_3,ushort *param_4,ulong *param_5,
          undefined2 *param_6,long param_7,undefined8 *param_8)

{
  undefined2 *puVar1;
  ushort uVar2;
  undefined8 uVar3;
  ulong uVar4;
  long lVar5;
  
  uVar4 = *(ulong *)(param_1 + 0x10);
  if ((*(byte *)(param_1 + 0x18) >> 1 & 1) != 0) {
    if (param_7 - (long)param_6 < 2) {
LAB_00c2aed8:
      uVar3 = 1;
      goto LAB_00c2af4c;
    }
    *param_6 = 0xfeff;
    param_6 = param_6 + 1;
  }
  if (param_3 < param_4) {
    lVar5 = param_7 - (long)param_6;
    do {
      uVar2 = *param_3;
      if ((uVar2 & 0xf800) == 0xd800 || uVar4 < uVar2) {
                    /* catch() { ... } // from try @ 00c2b038 with catch @ 00c2af48 */
        uVar3 = 2;
        goto LAB_00c2af4c;
      }
      if (lVar5 < 2) goto LAB_00c2aed8;
      param_3 = param_3 + 1;
      *(char *)param_6 = (char)uVar2;
                    /* catch() { ... } // from try @ 00c2ae8c with catch @ 00c2af20 */
      puVar1 = param_6 + 1;
      *(char *)((long)param_6 + 1) = (char)(uVar2 >> 8);
      param_6 = puVar1;
      lVar5 = lVar5 + -2;
    } while (param_3 < param_4);
    uVar3 = 0;
  }
  else {
    uVar3 = 0;
  }
LAB_00c2af4c:
  *param_5 = (ulong)param_3;
  *param_8 = param_6;
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c2aebc"></a> `00c2aebc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00c2aec0"></a> `00c2aec0` | `09 60 40 39` | ldrb w9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00c2aec4"></a> `00c2aec4` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00c2aec8"></a> `00c2aec8` | `09 01 08 36` | tbz w9,#0x1,0x00c2aee8 | `CONDITIONAL_JUMP`
<a id="insn-00c2aecc"></a> `00c2aecc` | `c9 00 05 cb` | sub x9,x6,x5 | `FALL_THROUGH`
<a id="insn-00c2aed0"></a> `00c2aed0` | `3f 09 00 f1` | cmp x9,#0x2 | `FALL_THROUGH`
<a id="insn-00c2aed4"></a> `00c2aed4` | `6a 00 00 54` | b.ge 0x00c2aee0 | `CONDITIONAL_JUMP`
<a id="insn-00c2aed8"></a> `00c2aed8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00c2aedc"></a> `00c2aedc` | `1c 00 00 14` | b 0x00c2af4c | `UNCONDITIONAL_JUMP`
<a id="insn-00c2aee0"></a> `00c2aee0` | `e9 df 9f 52` | mov w9,#0xfeff | `FALL_THROUGH`
<a id="insn-00c2aee4"></a> `00c2aee4` | `a9 24 00 78` | strh w9,[x5], #0x2 | `FALL_THROUGH`
<a id="insn-00c2aee8"></a> `00c2aee8` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00c2aeec"></a> `00c2aeec` | `a2 02 00 54` | b.cs 0x00c2af40 | `CONDITIONAL_JUMP`
<a id="insn-00c2aef0"></a> `00c2aef0` | `c9 00 05 cb` | sub x9,x6,x5 | `FALL_THROUGH`
<a id="insn-00c2aef4"></a> `00c2aef4` | `0a 00 9b 52` | mov w10,#0xd800 | `FALL_THROUGH`
<a id="insn-00c2aef8"></a> `00c2aef8` | `4b 00 40 79` | ldrh w11,[x2] | `FALL_THROUGH`
<a id="insn-00c2aefc"></a> `00c2aefc` | `6c 11 15 12` | and w12,w11,#0xf800 | `FALL_THROUGH`
<a id="insn-00c2af00"></a> `00c2af00` | `9f 01 0a 6b` | cmp w12,w10 | `FALL_THROUGH`
<a id="insn-00c2af04"></a> `00c2af04` | `00 11 4b fa` | ccmp x8,x11,#0x0,ne | `FALL_THROUGH`
<a id="insn-00c2af08"></a> `00c2af08` | `03 02 00 54` | b.cc 0x00c2af48 | `CONDITIONAL_JUMP`
<a id="insn-00c2af0c"></a> `00c2af0c` | `29 09 00 f1` | subs x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00c2af10"></a> `00c2af10` | `4b fe ff 54` | b.lt 0x00c2aed8 | `CONDITIONAL_JUMP`
<a id="insn-00c2af14"></a> `00c2af14` | `6c 7d 08 53` | lsr w12,w11,#0x8 | `FALL_THROUGH`
<a id="insn-00c2af18"></a> `00c2af18` | `42 08 00 91` | add x2,x2,#0x2 | `FALL_THROUGH`
<a id="insn-00c2af1c"></a> `00c2af1c` | `ab 00 00 39` | strb w11,[x5] | `FALL_THROUGH`
<a id="insn-00c2af20"></a> `00c2af20` | `ab 08 00 91` | add x11,x5,#0x2 | `FALL_THROUGH`
<a id="insn-00c2af24"></a> `00c2af24` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00c2af28"></a> `00c2af28` | `ac 04 00 39` | strb w12,[x5, #0x1] | `FALL_THROUGH`
<a id="insn-00c2af2c"></a> `00c2af2c` | `e5 03 0b aa` | mov x5,x11 | `FALL_THROUGH`
<a id="insn-00c2af30"></a> `00c2af30` | `43 fe ff 54` | b.cc 0x00c2aef8 | `CONDITIONAL_JUMP`
<a id="insn-00c2af34"></a> `00c2af34` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00c2af38"></a> `00c2af38` | `e5 03 0b aa` | mov x5,x11 | `FALL_THROUGH`
<a id="insn-00c2af3c"></a> `00c2af3c` | `04 00 00 14` | b 0x00c2af4c | `UNCONDITIONAL_JUMP`
<a id="insn-00c2af40"></a> `00c2af40` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00c2af44"></a> `00c2af44` | `02 00 00 14` | b 0x00c2af4c | `UNCONDITIONAL_JUMP`
<a id="insn-00c2af48"></a> `00c2af48` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00c2af4c"></a> `00c2af4c` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00c2af50"></a> `00c2af50` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00c2af54"></a> `00c2af54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c2aebc`](#insn-00c2aebc) 範囲 `[['00c2aebc', '00c2aecb']]`
  - `CONDITIONAL_JUMP` [`00c2aec8`](#insn-00c2aec8) → [`00c2aee8`](#insn-00c2aee8)
  - `FALL_THROUGH` [`00c2aec8`](#insn-00c2aec8) → [`00c2aecc`](#insn-00c2aecc)
- ブロック [`00c2aecc`](#insn-00c2aecc) 範囲 `[['00c2aecc', '00c2aed7']]`
  - `CONDITIONAL_JUMP` [`00c2aed4`](#insn-00c2aed4) → [`00c2aee0`](#insn-00c2aee0)
  - `FALL_THROUGH` [`00c2aed4`](#insn-00c2aed4) → [`00c2aed8`](#insn-00c2aed8)
- ブロック [`00c2aed8`](#insn-00c2aed8) 範囲 `[['00c2aed8', '00c2aedf']]`
  - `UNCONDITIONAL_JUMP` [`00c2aedc`](#insn-00c2aedc) → [`00c2af4c`](#insn-00c2af4c)
- ブロック [`00c2aee0`](#insn-00c2aee0) 範囲 `[['00c2aee0', '00c2aee7']]`
  - `FALL_THROUGH` [`00c2aee4`](#insn-00c2aee4) → [`00c2aee8`](#insn-00c2aee8)
- ブロック [`00c2aee8`](#insn-00c2aee8) 範囲 `[['00c2aee8', '00c2aeef']]`
  - `CONDITIONAL_JUMP` [`00c2aeec`](#insn-00c2aeec) → [`00c2af40`](#insn-00c2af40)
  - `FALL_THROUGH` [`00c2aeec`](#insn-00c2aeec) → [`00c2aef0`](#insn-00c2aef0)
- ブロック [`00c2aef0`](#insn-00c2aef0) 範囲 `[['00c2aef0', '00c2aef7']]`
  - `FALL_THROUGH` [`00c2aef4`](#insn-00c2aef4) → [`00c2aef8`](#insn-00c2aef8)
- ブロック [`00c2aef8`](#insn-00c2aef8) 範囲 `[['00c2aef8', '00c2af0b']]`
  - `CONDITIONAL_JUMP` [`00c2af08`](#insn-00c2af08) → [`00c2af48`](#insn-00c2af48)
  - `FALL_THROUGH` [`00c2af08`](#insn-00c2af08) → [`00c2af0c`](#insn-00c2af0c)
- ブロック [`00c2af0c`](#insn-00c2af0c) 範囲 `[['00c2af0c', '00c2af13']]`
  - `CONDITIONAL_JUMP` [`00c2af10`](#insn-00c2af10) → [`00c2aed8`](#insn-00c2aed8)
  - `FALL_THROUGH` [`00c2af10`](#insn-00c2af10) → [`00c2af14`](#insn-00c2af14)
- ブロック [`00c2af14`](#insn-00c2af14) 範囲 `[['00c2af14', '00c2af1f']]`
  - `FALL_THROUGH` [`00c2af1c`](#insn-00c2af1c) → [`00c2af20`](#insn-00c2af20)
- ブロック [`00c2af20`](#insn-00c2af20) 範囲 `[['00c2af20', '00c2af33']]`
  - `CONDITIONAL_JUMP` [`00c2af30`](#insn-00c2af30) → [`00c2aef8`](#insn-00c2aef8)
  - `FALL_THROUGH` [`00c2af30`](#insn-00c2af30) → [`00c2af34`](#insn-00c2af34)
- ブロック [`00c2af34`](#insn-00c2af34) 範囲 `[['00c2af34', '00c2af3f']]`
  - `UNCONDITIONAL_JUMP` [`00c2af3c`](#insn-00c2af3c) → [`00c2af4c`](#insn-00c2af4c)
- ブロック [`00c2af40`](#insn-00c2af40) 範囲 `[['00c2af40', '00c2af47']]`
  - `UNCONDITIONAL_JUMP` [`00c2af44`](#insn-00c2af44) → [`00c2af4c`](#insn-00c2af4c)
- ブロック [`00c2af48`](#insn-00c2af48) 範囲 `[['00c2af48', '00c2af4b']]`
  - `FALL_THROUGH` [`00c2af48`](#insn-00c2af48) → [`00c2af4c`](#insn-00c2af4c)
- ブロック [`00c2af4c`](#insn-00c2af4c) 範囲 `[['00c2af4c', '00c2af57']]`

## 命令位置別の参照

- [`00c2aec8`](#insn-00c2aec8) → [`00c2aee8`](#insn-00c2aee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2aed4`](#insn-00c2aed4) → [`00c2aee0`](#insn-00c2aee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2aedc`](#insn-00c2aedc) → [`00c2af4c`](#insn-00c2af4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2aeec`](#insn-00c2aeec) → [`00c2af40`](#insn-00c2af40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2af08`](#insn-00c2af08) → [`00c2af48`](#insn-00c2af48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2af10`](#insn-00c2af10) → [`00c2aed8`](#insn-00c2aed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2af30`](#insn-00c2af30) → [`00c2aef8`](#insn-00c2aef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2af3c`](#insn-00c2af3c) → [`00c2af4c`](#insn-00c2af4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c2af44`](#insn-00c2af44) → [`00c2af4c`](#insn-00c2af4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c2aec8`](#insn-00c2aec8)

~~~json
{
  "source": "00c2aec8",
  "target": "00c2aee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2aed4`](#insn-00c2aed4)

~~~json
{
  "source": "00c2aed4",
  "target": "00c2aee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2aedc`](#insn-00c2aedc)

~~~json
{
  "source": "00c2aedc",
  "target": "00c2af4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2aeec`](#insn-00c2aeec)

~~~json
{
  "source": "00c2aeec",
  "target": "00c2af40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2af08`](#insn-00c2af08)

~~~json
{
  "source": "00c2af08",
  "target": "00c2af48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2af10`](#insn-00c2af10)

~~~json
{
  "source": "00c2af10",
  "target": "00c2aed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2af30`](#insn-00c2af30)

~~~json
{
  "source": "00c2af30",
  "target": "00c2aef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2af3c`](#insn-00c2af3c)

~~~json
{
  "source": "00c2af3c",
  "target": "00c2af4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c2af44`](#insn-00c2af44)

~~~json
{
  "source": "00c2af44",
  "target": "00c2af4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
