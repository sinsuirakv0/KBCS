# 00b7defc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7dfc4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dfc4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0005.md#compare-35fb07033faf010495188d328b98c02f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7defc",
  "name": "FUN_00b7defc",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "55f615184c4d6a4169c4aeae97bf8e1b02e1305d096470d377d35b28daaa06ee",
  "source_text_sha256": "55f615184c4d6a4169c4aeae97bf8e1b02e1305d096470d377d35b28daaa06ee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7defc",
        "00b7df6f"
      ]
    ],
    "bytes_sha256": "c83e9626803d69025cb99ba1634f81eeae0c786b058819a3a623733754472744",
    "instruction_count": 29,
    "instruction_bytes": 116,
    "body_bytes": 116,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00b7b694](../00b7b/00b7b694.md)
- [00bdaf40](../00bda/00bdaf40.md)

## 関連文字列（未確認候補）

~~~text
"unspecified iostream_category error"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1054 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00b7defc(undefined8 *param_1,undefined8 param_2,int param_3)

{
  undefined8 uVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  char *pcVar7;
  
  if ((param_3 != 1) && (param_3 < 0x1000)) {
    FUN_00b7b694();
    return;
  }
  pcVar7 = (char *)_Znwm(0x28);
  param_1[2] = pcVar7;
  uVar6 = _UNK_002b1018;
  uVar5 = _DAT_002b1010;
  uVar4 = s_unspecified_iostream_category_er_002ad6de._24_8_;
  uVar3 = s_unspecified_iostream_category_er_002ad6de._16_8_;
  uVar2 = s_unspecified_iostream_category_er_002ad6de._8_8_;
  uVar1 = s_unspecified_iostream_category_er_002ad6de._0_8_;
  pcVar7[0x1f] = 'r';
  pcVar7[0x20] = 'r';
  pcVar7[0x21] = 'o';
  pcVar7[0x22] = 'r';
  param_1[1] = uVar6;
  *param_1 = uVar5;
  *(undefined8 *)(pcVar7 + 8) = uVar2;
  *(undefined8 *)pcVar7 = uVar1;
  *(undefined8 *)(pcVar7 + 0x18) = uVar4;
  *(undefined8 *)(pcVar7 + 0x10) = uVar3;
  pcVar7[0x23] = '\0';
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7defc"></a> `00b7defc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00b7df00"></a> `00b7df00` | `3f 04 00 71` | cmp w1,#0x1 | `FALL_THROUGH`
<a id="insn-00b7df04"></a> `00b7df04` | `80 00 00 54` | b.eq 0x00b7df14 | `CONDITIONAL_JUMP`
<a id="insn-00b7df08"></a> `00b7df08` | `3f fc 3f 71` | cmp w1,#0xfff | `FALL_THROUGH`
<a id="insn-00b7df0c"></a> `00b7df0c` | `4c 00 00 54` | b.gt 0x00b7df14 | `CONDITIONAL_JUMP`
<a id="insn-00b7df10"></a> `00b7df10` | `e1 f5 ff 17` | b 0x00b7b694 | `CALL_TERMINATOR`
<a id="insn-00b7df14"></a> `00b7df14` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b7df18"></a> `00b7df18` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b7df1c"></a> `00b7df1c` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7df20"></a> `00b7df20` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b7df24"></a> `00b7df24` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00b7df28"></a> `00b7df28` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00b7df2c"></a> `00b7df2c` | `05 74 01 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00b7df30"></a> `00b7df30` | `a8 b9 ff 90` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00b7df34"></a> `00b7df34` | `49 4e 8e 52` | mov w9,#0x7272 | `FALL_THROUGH`
<a id="insn-00b7df38"></a> `00b7df38` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b7df3c"></a> `00b7df3c` | `00 05 c0 3d` | ldr q0,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b7df40"></a> `00b7df40` | `88 b9 ff 90` | adrp x8,0x2ad000 | `FALL_THROUGH`
<a id="insn-00b7df44"></a> `00b7df44` | `08 79 1b 91` | add x8,x8,#0x6de | `FALL_THROUGH`
<a id="insn-00b7df48"></a> `00b7df48` | `01 09 40 ad` | ldp q1,q2,[x8] | `FALL_THROUGH`
<a id="insn-00b7df4c"></a> `00b7df4c` | `e9 4d ae 72` | movk w9,#0x726f, LSL #16 | `FALL_THROUGH`
<a id="insn-00b7df50"></a> `00b7df50` | `09 f0 01 b8` | stur w9,[x0, #0x1f] | `FALL_THROUGH`
<a id="insn-00b7df54"></a> `00b7df54` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00b7df58"></a> `00b7df58` | `01 08 00 ad` | stp q1,q2,[x0] | `FALL_THROUGH`
<a id="insn-00b7df5c"></a> `00b7df5c` | `1f 8c 00 39` | strb wzr,[x0, #0x23] | `FALL_THROUGH`
<a id="insn-00b7df60"></a> `00b7df60` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7df64"></a> `00b7df64` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b7df68"></a> `00b7df68` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b7df6c"></a> `00b7df6c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7defc`](#insn-00b7defc) 範囲 `[['00b7defc', '00b7df07']]`
  - `CONDITIONAL_JUMP` [`00b7df04`](#insn-00b7df04) → [`00b7df14`](#insn-00b7df14)
  - `FALL_THROUGH` [`00b7df04`](#insn-00b7df04) → [`00b7df08`](#insn-00b7df08)
- ブロック [`00b7df08`](#insn-00b7df08) 範囲 `[['00b7df08', '00b7df0f']]`
  - `CONDITIONAL_JUMP` [`00b7df0c`](#insn-00b7df0c) → [`00b7df14`](#insn-00b7df14)
  - `FALL_THROUGH` [`00b7df0c`](#insn-00b7df0c) → [`00b7df10`](#insn-00b7df10)
- ブロック [`00b7df10`](#insn-00b7df10) 範囲 `[['00b7df10', '00b7df13']]`
- ブロック [`00b7df14`](#insn-00b7df14) 範囲 `[['00b7df14', '00b7df6f']]`

## 命令位置別の参照

- [`00b7df04`](#insn-00b7df04) → [`00b7df14`](#insn-00b7df14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7df0c`](#insn-00b7df0c) → [`00b7df14`](#insn-00b7df14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7df10`](#insn-00b7df10) → [`00b7b694`](../00b7b/00b7b694.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b7b694` · 推定シンボル `None` · 推定型 `None`
- [`00b7df18`](#insn-00b7df18) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7df1c`](#insn-00b7df1c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7df2c`](#insn-00b7df2c) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00b7df3c`](#insn-00b7df3c) → `002b1010`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7df48`](#insn-00b7df48) → `002ad6de`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b7df48`](#insn-00b7df48) → `002ad6ee`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b7df60`](#insn-00b7df60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7df64`](#insn-00b7df64) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7df04`](#insn-00b7df04)

~~~json
{
  "source": "00b7df04",
  "target": "00b7df14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7df0c`](#insn-00b7df0c)

~~~json
{
  "source": "00b7df0c",
  "target": "00b7df14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7df10`](#insn-00b7df10)

~~~json
{
  "source": "00b7df10",
  "target": "00b7b694",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7df18`](#insn-00b7df18)

~~~json
{
  "source": "00b7df18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7df1c`](#insn-00b7df1c)

~~~json
{
  "source": "00b7df1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7df2c`](#insn-00b7df2c)

~~~json
{
  "source": "00b7df2c",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7df3c`](#insn-00b7df3c)

~~~json
{
  "source": "00b7df3c",
  "target": "002b1010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7df48`](#insn-00b7df48)

~~~json
{
  "source": "00b7df48",
  "target": "002ad6de",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad6de",
  "offset": 0,
  "size": 36,
  "datatype": "string",
  "bytes": "756e73706563696669656420696f73747265616d5f63617465676f7279206572",
  "capture_start": "002ad6de",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b7df48`](#insn-00b7df48)

~~~json
{
  "source": "00b7df48",
  "target": "002ad6ee",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad6de",
  "offset": 16,
  "size": 36,
  "datatype": "string",
  "bytes": "756e73706563696669656420696f73747265616d5f63617465676f7279206572",
  "capture_start": "002ad6de",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b7df60`](#insn-00b7df60)

~~~json
{
  "source": "00b7df60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7df64`](#insn-00b7df64)

~~~json
{
  "source": "00b7df64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
