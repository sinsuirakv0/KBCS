# 00bada1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00badae4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00badae4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-0fea35f939e55c52ebfc999aeca59f01)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bada1c",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56e37d97520430703b4a2a4e86975cef5c4932a49ee7a31d69e3ac0b528d76d9",
  "source_text_sha256": "56e37d97520430703b4a2a4e86975cef5c4932a49ee7a31d69e3ac0b528d76d9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bada1c",
        "00badaef"
      ]
    ],
    "bytes_sha256": "06c671ab25216d05790a04a670c179d698088658f0e39e259f71bb1c68eb9041",
    "instruction_count": 53,
    "instruction_bytes": 212,
    "body_bytes": 212,
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

## 疑似コード / UTF-8 1388 bytes

~~~c

undefined8
_ZNKSt6__ndk115__codecvt_utf16IwLb1EE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_
          (long param_1,undefined8 param_2,uint *param_3,uint *param_4,undefined8 *param_5,
          byte *param_6,long param_7,undefined8 *param_8)

{
  int iVar1;
  uint uVar2;
  undefined8 uVar3;
  byte *pbVar4;
  ulong uVar5;
  
  uVar5 = *(ulong *)(param_1 + 0x18);
  if ((*(byte *)(param_1 + 0x20) >> 1 & 1) != 0) {
    if (param_7 - (long)param_6 < 2) {
LAB_00bada38:
      uVar3 = 1;
      goto LAB_00badae4;
    }
    param_6[0] = 0xff;
    param_6[1] = 0xfe;
    param_6 = param_6 + 2;
  }
  for (; param_3 < param_4; param_3 = param_3 + 1) {
    uVar2 = *param_3;
    if (uVar2 >> 0xb == 0x1b || uVar5 < uVar2) {
      uVar3 = 2;
      goto LAB_00badae4;
    }
    if ((uVar2 & 0xffff0000) == 0) {
      if (param_7 - (long)param_6 < 2) goto LAB_00bada38;
      pbVar4 = param_6 + 2;
      *(short *)param_6 = (short)uVar2;
    }
    else {
      if (param_7 - (long)param_6 < 4) goto LAB_00bada38;
      param_6[2] = (byte)uVar2;
      iVar1 = (uVar2 >> 10 & 0x7c0) + 0x3fc0;
      param_6[3] = (byte)(uVar2 >> 8) & 3 | 0xdc;
      pbVar4 = param_6 + 4;
      *param_6 = (byte)iVar1 | (byte)(uVar2 >> 10) & 0x3f;
      param_6[1] = (byte)((uint)iVar1 >> 8) | 0xd8;
    }
    param_6 = pbVar4;
  }
  uVar3 = 0;
LAB_00badae4:
  *param_5 = param_3;
  *param_8 = param_6;
  return uVar3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bada1c"></a> `00bada1c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bada20"></a> `00bada20` | `09 80 40 39` | ldrb w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bada24"></a> `00bada24` | `08 0c 40 f9` | ldr x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bada28"></a> `00bada28` | `09 01 08 36` | tbz w9,#0x1,0x00bada48 | `CONDITIONAL_JUMP`
<a id="insn-00bada2c"></a> `00bada2c` | `c9 00 05 cb` | sub x9,x6,x5 | `FALL_THROUGH`
<a id="insn-00bada30"></a> `00bada30` | `3f 09 00 f1` | cmp x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bada34"></a> `00bada34` | `6a 00 00 54` | b.ge 0x00bada40 | `CONDITIONAL_JUMP`
<a id="insn-00bada38"></a> `00bada38` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bada3c"></a> `00bada3c` | `2a 00 00 14` | b 0x00badae4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bada40"></a> `00bada40` | `e9 df 9f 52` | mov w9,#0xfeff | `FALL_THROUGH`
<a id="insn-00bada44"></a> `00bada44` | `a9 24 00 78` | strh w9,[x5], #0x2 | `FALL_THROUGH`
<a id="insn-00bada48"></a> `00bada48` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00bada4c"></a> `00bada4c` | `62 04 00 54` | b.cs 0x00badad8 | `CONDITIONAL_JUMP`
<a id="insn-00bada50"></a> `00bada50` | `09 f8 87 52` | mov w9,#0x3fc0 | `FALL_THROUGH`
<a id="insn-00bada54"></a> `00bada54` | `0a 1b 80 52` | mov w10,#0xd8 | `FALL_THROUGH`
<a id="insn-00bada58"></a> `00bada58` | `04 00 00 14` | b 0x00bada68 | `UNCONDITIONAL_JUMP`
<a id="insn-00bada5c"></a> `00bada5c` | `42 10 00 91` | add x2,x2,#0x4 | `FALL_THROUGH`
<a id="insn-00bada60"></a> `00bada60` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00bada64"></a> `00bada64` | `a2 03 00 54` | b.cs 0x00badad8 | `CONDITIONAL_JUMP`
<a id="insn-00bada68"></a> `00bada68` | `4b 00 40 b9` | ldr w11,[x2] | `FALL_THROUGH`
<a id="insn-00bada6c"></a> `00bada6c` | `6c 7d 0b 53` | lsr w12,w11,#0xb | `FALL_THROUGH`
<a id="insn-00bada70"></a> `00bada70` | `9f 6d 00 71` | cmp w12,#0x1b | `FALL_THROUGH`
<a id="insn-00bada74"></a> `00bada74` | `00 11 4b fa` | ccmp x8,x11,#0x0,ne | `FALL_THROUGH`
<a id="insn-00bada78"></a> `00bada78` | `43 03 00 54` | b.cc 0x00badae0 | `CONDITIONAL_JUMP`
<a id="insn-00bada7c"></a> `00bada7c` | `6d 7d 10 53` | lsr w13,w11,#0x10 | `FALL_THROUGH`
<a id="insn-00bada80"></a> `00bada80` | `cc 00 05 cb` | sub x12,x6,x5 | `FALL_THROUGH`
<a id="insn-00bada84"></a> `00bada84` | `ad 00 00 35` | cbnz w13,0x00bada98 | `CONDITIONAL_JUMP`
<a id="insn-00bada88"></a> `00bada88` | `9f 09 00 f1` | cmp x12,#0x2 | `FALL_THROUGH`
<a id="insn-00bada8c"></a> `00bada8c` | `6b fd ff 54` | b.lt 0x00bada38 | `CONDITIONAL_JUMP`
<a id="insn-00bada90"></a> `00bada90` | `ab 24 00 78` | strh w11,[x5], #0x2 | `FALL_THROUGH`
<a id="insn-00bada94"></a> `00bada94` | `f2 ff ff 17` | b 0x00bada5c | `UNCONDITIONAL_JUMP`
<a id="insn-00bada98"></a> `00bada98` | `9f 11 00 f1` | cmp x12,#0x4 | `FALL_THROUGH`
<a id="insn-00bada9c"></a> `00bada9c` | `eb fc ff 54` | b.lt 0x00bada38 | `CONDITIONAL_JUMP`
<a id="insn-00badaa0"></a> `00badaa0` | `6c 7d 0a 53` | lsr w12,w11,#0xa | `FALL_THROUGH`
<a id="insn-00badaa4"></a> `00badaa4` | `8e 1b 80 52` | mov w14,#0xdc | `FALL_THROUGH`
<a id="insn-00badaa8"></a> `00badaa8` | `ab 08 00 39` | strb w11,[x5, #0x2] | `FALL_THROUGH`
<a id="insn-00badaac"></a> `00badaac` | `6e 25 08 33` | bfxil w14,w11,#0x8,#0x2 | `FALL_THROUGH`
<a id="insn-00badab0"></a> `00badab0` | `8c 11 1a 12` | and w12,w12,#0x7c0 | `FALL_THROUGH`
<a id="insn-00badab4"></a> `00badab4` | `8c 01 09 0b` | add w12,w12,w9 | `FALL_THROUGH`
<a id="insn-00badab8"></a> `00badab8` | `ae 0c 00 39` | strb w14,[x5, #0x3] | `FALL_THROUGH`
<a id="insn-00badabc"></a> `00badabc` | `4d 21 4c 2a` | orr w13,w10,w12, LSR #0x8 | `FALL_THROUGH`
<a id="insn-00badac0"></a> `00badac0` | `6c 3d 0a 33` | bfxil w12,w11,#0xa,#0x6 | `FALL_THROUGH`
<a id="insn-00badac4"></a> `00badac4` | `ab 10 00 91` | add x11,x5,#0x4 | `FALL_THROUGH`
<a id="insn-00badac8"></a> `00badac8` | `ac 00 00 39` | strb w12,[x5] | `FALL_THROUGH`
<a id="insn-00badacc"></a> `00badacc` | `ad 04 00 39` | strb w13,[x5, #0x1] | `FALL_THROUGH`
<a id="insn-00badad0"></a> `00badad0` | `e5 03 0b aa` | mov x5,x11 | `FALL_THROUGH`
<a id="insn-00badad4"></a> `00badad4` | `e2 ff ff 17` | b 0x00bada5c | `UNCONDITIONAL_JUMP`
<a id="insn-00badad8"></a> `00badad8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00badadc"></a> `00badadc` | `02 00 00 14` | b 0x00badae4 | `UNCONDITIONAL_JUMP`
<a id="insn-00badae0"></a> `00badae0` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00badae4"></a> `00badae4` | `82 00 00 f9` | str x2,[x4] | `FALL_THROUGH`
<a id="insn-00badae8"></a> `00badae8` | `e5 00 00 f9` | str x5,[x7] | `FALL_THROUGH`
<a id="insn-00badaec"></a> `00badaec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bada1c`](#insn-00bada1c) 範囲 `[['00bada1c', '00bada2b']]`
  - `CONDITIONAL_JUMP` [`00bada28`](#insn-00bada28) → [`00bada48`](#insn-00bada48)
  - `FALL_THROUGH` [`00bada28`](#insn-00bada28) → [`00bada2c`](#insn-00bada2c)
- ブロック [`00bada2c`](#insn-00bada2c) 範囲 `[['00bada2c', '00bada37']]`
  - `CONDITIONAL_JUMP` [`00bada34`](#insn-00bada34) → [`00bada40`](#insn-00bada40)
  - `FALL_THROUGH` [`00bada34`](#insn-00bada34) → [`00bada38`](#insn-00bada38)
- ブロック [`00bada38`](#insn-00bada38) 範囲 `[['00bada38', '00bada3f']]`
  - `UNCONDITIONAL_JUMP` [`00bada3c`](#insn-00bada3c) → [`00badae4`](#insn-00badae4)
- ブロック [`00bada40`](#insn-00bada40) 範囲 `[['00bada40', '00bada47']]`
  - `FALL_THROUGH` [`00bada44`](#insn-00bada44) → [`00bada48`](#insn-00bada48)
- ブロック [`00bada48`](#insn-00bada48) 範囲 `[['00bada48', '00bada4f']]`
  - `CONDITIONAL_JUMP` [`00bada4c`](#insn-00bada4c) → [`00badad8`](#insn-00badad8)
  - `FALL_THROUGH` [`00bada4c`](#insn-00bada4c) → [`00bada50`](#insn-00bada50)
- ブロック [`00bada50`](#insn-00bada50) 範囲 `[['00bada50', '00bada5b']]`
  - `UNCONDITIONAL_JUMP` [`00bada58`](#insn-00bada58) → [`00bada68`](#insn-00bada68)
- ブロック [`00bada5c`](#insn-00bada5c) 範囲 `[['00bada5c', '00bada67']]`
  - `CONDITIONAL_JUMP` [`00bada64`](#insn-00bada64) → [`00badad8`](#insn-00badad8)
  - `FALL_THROUGH` [`00bada64`](#insn-00bada64) → [`00bada68`](#insn-00bada68)
- ブロック [`00bada68`](#insn-00bada68) 範囲 `[['00bada68', '00bada7b']]`
  - `CONDITIONAL_JUMP` [`00bada78`](#insn-00bada78) → [`00badae0`](#insn-00badae0)
  - `FALL_THROUGH` [`00bada78`](#insn-00bada78) → [`00bada7c`](#insn-00bada7c)
- ブロック [`00bada7c`](#insn-00bada7c) 範囲 `[['00bada7c', '00bada87']]`
  - `CONDITIONAL_JUMP` [`00bada84`](#insn-00bada84) → [`00bada98`](#insn-00bada98)
  - `FALL_THROUGH` [`00bada84`](#insn-00bada84) → [`00bada88`](#insn-00bada88)
- ブロック [`00bada88`](#insn-00bada88) 範囲 `[['00bada88', '00bada8f']]`
  - `CONDITIONAL_JUMP` [`00bada8c`](#insn-00bada8c) → [`00bada38`](#insn-00bada38)
  - `FALL_THROUGH` [`00bada8c`](#insn-00bada8c) → [`00bada90`](#insn-00bada90)
- ブロック [`00bada90`](#insn-00bada90) 範囲 `[['00bada90', '00bada97']]`
  - `UNCONDITIONAL_JUMP` [`00bada94`](#insn-00bada94) → [`00bada5c`](#insn-00bada5c)
- ブロック [`00bada98`](#insn-00bada98) 範囲 `[['00bada98', '00bada9f']]`
  - `CONDITIONAL_JUMP` [`00bada9c`](#insn-00bada9c) → [`00bada38`](#insn-00bada38)
  - `FALL_THROUGH` [`00bada9c`](#insn-00bada9c) → [`00badaa0`](#insn-00badaa0)
- ブロック [`00badaa0`](#insn-00badaa0) 範囲 `[['00badaa0', '00badad7']]`
  - `UNCONDITIONAL_JUMP` [`00badad4`](#insn-00badad4) → [`00bada5c`](#insn-00bada5c)
- ブロック [`00badad8`](#insn-00badad8) 範囲 `[['00badad8', '00badadf']]`
  - `UNCONDITIONAL_JUMP` [`00badadc`](#insn-00badadc) → [`00badae4`](#insn-00badae4)
- ブロック [`00badae0`](#insn-00badae0) 範囲 `[['00badae0', '00badae3']]`
  - `FALL_THROUGH` [`00badae0`](#insn-00badae0) → [`00badae4`](#insn-00badae4)
- ブロック [`00badae4`](#insn-00badae4) 範囲 `[['00badae4', '00badaef']]`

## 命令位置別の参照

- [`00bada28`](#insn-00bada28) → [`00bada48`](#insn-00bada48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bada34`](#insn-00bada34) → [`00bada40`](#insn-00bada40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bada3c`](#insn-00bada3c) → [`00badae4`](#insn-00badae4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bada4c`](#insn-00bada4c) → [`00badad8`](#insn-00badad8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bada58`](#insn-00bada58) → [`00bada68`](#insn-00bada68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bada64`](#insn-00bada64) → [`00badad8`](#insn-00badad8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bada78`](#insn-00bada78) → [`00badae0`](#insn-00badae0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bada84`](#insn-00bada84) → [`00bada98`](#insn-00bada98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bada8c`](#insn-00bada8c) → [`00bada38`](#insn-00bada38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bada94`](#insn-00bada94) → [`00bada5c`](#insn-00bada5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bada9c`](#insn-00bada9c) → [`00bada38`](#insn-00bada38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badad4`](#insn-00badad4) → [`00bada5c`](#insn-00bada5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00badadc`](#insn-00badadc) → [`00badae4`](#insn-00badae4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bada28`](#insn-00bada28)

~~~json
{
  "source": "00bada28",
  "target": "00bada48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bada34`](#insn-00bada34)

~~~json
{
  "source": "00bada34",
  "target": "00bada40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bada3c`](#insn-00bada3c)

~~~json
{
  "source": "00bada3c",
  "target": "00badae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bada4c`](#insn-00bada4c)

~~~json
{
  "source": "00bada4c",
  "target": "00badad8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bada58`](#insn-00bada58)

~~~json
{
  "source": "00bada58",
  "target": "00bada68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bada64`](#insn-00bada64)

~~~json
{
  "source": "00bada64",
  "target": "00badad8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bada78`](#insn-00bada78)

~~~json
{
  "source": "00bada78",
  "target": "00badae0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bada84`](#insn-00bada84)

~~~json
{
  "source": "00bada84",
  "target": "00bada98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bada8c`](#insn-00bada8c)

~~~json
{
  "source": "00bada8c",
  "target": "00bada38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bada94`](#insn-00bada94)

~~~json
{
  "source": "00bada94",
  "target": "00bada5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bada9c`](#insn-00bada9c)

~~~json
{
  "source": "00bada9c",
  "target": "00bada38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badad4`](#insn-00badad4)

~~~json
{
  "source": "00badad4",
  "target": "00bada5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00badadc`](#insn-00badadc)

~~~json
{
  "source": "00badadc",
  "target": "00badae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
