# 00a3fcac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a3ecb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3e/00a3ecb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0062.md#compare-b14c2b3bc6b0943e181a2e384db8fc5b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3fcac",
  "name": "FUN_00a3fcac",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "891c5fed07ef7a62a7e4a73a02d5c44b3e7a8c8f8612702893034d5e20e44085",
  "source_text_sha256": "891c5fed07ef7a62a7e4a73a02d5c44b3e7a8c8f8612702893034d5e20e44085",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3fcac",
        "00a3fd63"
      ]
    ],
    "bytes_sha256": "65b60e4d722246a2269f7191dc48c78908afa1b43d5d1b40efc57a04e680d3ef",
    "instruction_count": 46,
    "instruction_bytes": 184,
    "body_bytes": 184,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a3f914](../00a3f/00a3f914.md)
- [00a3f968](../00a3f/00a3f968.md)

## 呼び出し先

- [0043be80](../0043b/0043be80.md)
- [00691c08](../00691/00691c08.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 873 bytes

~~~c

void FUN_00a3fcac(undefined8 *param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  *param_1 = *param_2;
  if ((*(byte *)(param_2 + 1) & 1) == 0) {
    uVar2 = param_2[2];
    uVar1 = param_2[1];
    param_1[3] = param_2[3];
    param_1[2] = uVar2;
    param_1[1] = uVar1;
  }
  else {
    FUN_0043be80(param_1 + 1,param_2[3],param_2[2]);
  }
  param_1[5] = 0;
  param_1[4] = param_1 + 5;
  param_1[6] = 0;
                    /* catch() { ... } // from try @ 00a3dd3c with catch @ 00a3fd18 */
  FUN_00691c08(param_1 + 4,param_2[4],param_2 + 5);
                    /* catch() { ... } // from try @ 00a3dcf0 with catch @ 00a3fd30 */
  param_1[8] = 0;
  param_1[7] = param_1 + 8;
                    /* catch() { ... } // from try @ 00a3dd00 with catch @ 00a3fd38 */
  param_1[9] = 0;
  FUN_00691c08(param_1 + 7,param_2[7],param_2 + 8);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3fcac"></a> `00a3fcac` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00a3fcb0"></a> `00a3fcb0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3fcb4"></a> `00a3fcb4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3fcb8"></a> `00a3fcb8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3fcbc"></a> `00a3fcbc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a3fcc0"></a> `00a3fcc0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3fcc4"></a> `00a3fcc4` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00a3fcc8"></a> `00a3fcc8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00a3fccc"></a> `00a3fccc` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00a3fcd0"></a> `00a3fcd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a3fcd4"></a> `00a3fcd4` | `88 86 00 f8` | str x8,[x20], #0x8 | `FALL_THROUGH`
<a id="insn-00a3fcd8"></a> `00a3fcd8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00a3fcdc"></a> `00a3fcdc` | `09 8d 40 38` | ldrb w9,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00a3fce0"></a> `00a3fce0` | `c9 00 00 37` | tbnz w9,#0x0,0x00a3fcf8 | `CONDITIONAL_JUMP`
<a id="insn-00a3fce4"></a> `00a3fce4` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a3fce8"></a> `00a3fce8` | `00 01 c0 3d` | ldr q0,[x8] | `FALL_THROUGH`
<a id="insn-00a3fcec"></a> `00a3fcec` | `89 0a 00 f9` | str x9,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00a3fcf0"></a> `00a3fcf0` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00a3fcf4"></a> `00a3fcf4` | `04 00 00 14` | b 0x00a3fd04 | `UNCONDITIONAL_JUMP`
<a id="insn-00a3fcf8"></a> `00a3fcf8` | `c2 06 41 a9` | ldp x2,x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00a3fcfc"></a> `00a3fcfc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a3fd00"></a> `00a3fd00` | `60 f0 e7 97` | bl 0x0043be80 | `UNCONDITIONAL_CALL`
<a id="insn-00a3fd04"></a> `00a3fd04` | `f8 03 13 aa` | mov x24,x19 | `FALL_THROUGH`
<a id="insn-00a3fd08"></a> `00a3fd08` | `f5 03 13 aa` | mov x21,x19 | `FALL_THROUGH`
<a id="insn-00a3fd0c"></a> `00a3fd0c` | `1f 8f 02 f8` | str xzr,[x24, #0x28]! | `FALL_THROUGH`
<a id="insn-00a3fd10"></a> `00a3fd10` | `b8 0e 02 f8` | str x24,[x21, #0x20]! | `FALL_THROUGH`
<a id="insn-00a3fd14"></a> `00a3fd14` | `bf 0a 00 f9` | str xzr,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00a3fd18"></a> `00a3fd18` | `c1 12 40 f9` | ldr x1,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00a3fd1c"></a> `00a3fd1c` | `c2 a2 00 91` | add x2,x22,#0x28 | `FALL_THROUGH`
<a id="insn-00a3fd20"></a> `00a3fd20` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a3fd24"></a> `00a3fd24` | `b9 47 f1 97` | bl 0x00691c08 | `UNCONDITIONAL_CALL`
<a id="insn-00a3fd28"></a> `00a3fd28` | `f9 03 13 aa` | mov x25,x19 | `FALL_THROUGH`
<a id="insn-00a3fd2c"></a> `00a3fd2c` | `f7 03 13 aa` | mov x23,x19 | `FALL_THROUGH`
<a id="insn-00a3fd30"></a> `00a3fd30` | `3f 0f 04 f8` | str xzr,[x25, #0x40]! | `FALL_THROUGH`
<a id="insn-00a3fd34"></a> `00a3fd34` | `f9 8e 03 f8` | str x25,[x23, #0x38]! | `FALL_THROUGH`
<a id="insn-00a3fd38"></a> `00a3fd38` | `ff 0a 00 f9` | str xzr,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00a3fd3c"></a> `00a3fd3c` | `c1 1e 40 f9` | ldr x1,[x22, #0x38] | `FALL_THROUGH`
<a id="insn-00a3fd40"></a> `00a3fd40` | `c2 02 01 91` | add x2,x22,#0x40 | `FALL_THROUGH`
<a id="insn-00a3fd44"></a> `00a3fd44` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00a3fd48"></a> `00a3fd48` | `b0 47 f1 97` | bl 0x00691c08 | `UNCONDITIONAL_CALL`
<a id="insn-00a3fd4c"></a> `00a3fd4c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a3fd50"></a> `00a3fd50` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3fd54"></a> `00a3fd54` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a3fd58"></a> `00a3fd58` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a3fd5c"></a> `00a3fd5c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00a3fd60"></a> `00a3fd60` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3fcac`](#insn-00a3fcac) 範囲 `[['00a3fcac', '00a3fce3']]`
  - `CONDITIONAL_JUMP` [`00a3fce0`](#insn-00a3fce0) → [`00a3fcf8`](#insn-00a3fcf8)
  - `FALL_THROUGH` [`00a3fce0`](#insn-00a3fce0) → [`00a3fce4`](#insn-00a3fce4)
- ブロック [`00a3fce4`](#insn-00a3fce4) 範囲 `[['00a3fce4', '00a3fcf7']]`
  - `UNCONDITIONAL_JUMP` [`00a3fcf4`](#insn-00a3fcf4) → [`00a3fd04`](#insn-00a3fd04)
- ブロック [`00a3fcf8`](#insn-00a3fcf8) 範囲 `[['00a3fcf8', '00a3fd03']]`
  - `FALL_THROUGH` [`00a3fd00`](#insn-00a3fd00) → [`00a3fd04`](#insn-00a3fd04)
- ブロック [`00a3fd04`](#insn-00a3fd04) 範囲 `[['00a3fd04', '00a3fd17']]`
  - `FALL_THROUGH` [`00a3fd14`](#insn-00a3fd14) → [`00a3fd18`](#insn-00a3fd18)
- ブロック [`00a3fd18`](#insn-00a3fd18) 範囲 `[['00a3fd18', '00a3fd2f']]`
  - `FALL_THROUGH` [`00a3fd2c`](#insn-00a3fd2c) → [`00a3fd30`](#insn-00a3fd30)
- ブロック [`00a3fd30`](#insn-00a3fd30) 範囲 `[['00a3fd30', '00a3fd37']]`
  - `FALL_THROUGH` [`00a3fd34`](#insn-00a3fd34) → [`00a3fd38`](#insn-00a3fd38)
- ブロック [`00a3fd38`](#insn-00a3fd38) 範囲 `[['00a3fd38', '00a3fd63']]`

## 命令位置別の参照

- [`00a3fcac`](#insn-00a3fcac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3fcb0`](#insn-00a3fcb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3fcb4`](#insn-00a3fcb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3fcb8`](#insn-00a3fcb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3fcbc`](#insn-00a3fcbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3fce0`](#insn-00a3fce0) → [`00a3fcf8`](#insn-00a3fcf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3fcf4`](#insn-00a3fcf4) → [`00a3fd04`](#insn-00a3fd04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3fd00`](#insn-00a3fd00) → [`0043be80`](../0043b/0043be80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043be80` · 推定シンボル `None` · 推定型 `None`
- [`00a3fd24`](#insn-00a3fd24) → [`00691c08`](../00691/00691c08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00691c08` · 推定シンボル `None` · 推定型 `None`
- [`00a3fd48`](#insn-00a3fd48) → [`00691c08`](../00691/00691c08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00691c08` · 推定シンボル `None` · 推定型 `None`
- [`00a3fd4c`](#insn-00a3fd4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3fd50`](#insn-00a3fd50) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3fd54`](#insn-00a3fd54) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3fd58`](#insn-00a3fd58) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3fd5c`](#insn-00a3fd5c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3fcac`](#insn-00a3fcac)

~~~json
{
  "source": "00a3fcac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3fcb0`](#insn-00a3fcb0)

~~~json
{
  "source": "00a3fcb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3fcb4`](#insn-00a3fcb4)

~~~json
{
  "source": "00a3fcb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3fcb8`](#insn-00a3fcb8)

~~~json
{
  "source": "00a3fcb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3fcbc`](#insn-00a3fcbc)

~~~json
{
  "source": "00a3fcbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3fce0`](#insn-00a3fce0)

~~~json
{
  "source": "00a3fce0",
  "target": "00a3fcf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3fcf4`](#insn-00a3fcf4)

~~~json
{
  "source": "00a3fcf4",
  "target": "00a3fd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3fd00`](#insn-00a3fd00)

~~~json
{
  "source": "00a3fd00",
  "target": "0043be80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3fd24`](#insn-00a3fd24)

~~~json
{
  "source": "00a3fd24",
  "target": "00691c08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3fd48`](#insn-00a3fd48)

~~~json
{
  "source": "00a3fd48",
  "target": "00691c08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3fd4c`](#insn-00a3fd4c)

~~~json
{
  "source": "00a3fd4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3fd50`](#insn-00a3fd50)

~~~json
{
  "source": "00a3fd50",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3fd54`](#insn-00a3fd54)

~~~json
{
  "source": "00a3fd54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3fd58`](#insn-00a3fd58)

~~~json
{
  "source": "00a3fd58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3fd5c`](#insn-00a3fd5c)

~~~json
{
  "source": "00a3fd5c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
