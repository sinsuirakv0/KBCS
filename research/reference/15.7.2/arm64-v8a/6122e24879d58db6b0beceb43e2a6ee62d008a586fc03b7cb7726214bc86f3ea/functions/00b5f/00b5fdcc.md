# 00b5fdcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b5fe94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fe94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0069.md#compare-c7c945112aa8b428800f00c46229c6b9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5fdcc",
  "name": "_ZN8firebase4auth4Auth11UseEmulatorENSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEj",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d5a9317eb64ea714d1a31bd7ce6cf90ea3be025884cf750519cf8c635d8cfe90",
  "source_text_sha256": "d5a9317eb64ea714d1a31bd7ce6cf90ea3be025884cf750519cf8c635d8cfe90",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5fdcc",
        "00b5fe5b"
      ]
    ],
    "bytes_sha256": "78a9005ad397945cb20fe6e2c01340b886b54b5a6240af740e80d54e196e56a9",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bddfe0](../00bdd/00bddfe0.md)
- [00bde100](../00bde/00bde100.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1635 bytes

~~~c

void _ZN8firebase4auth4Auth11UseEmulatorENSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEj
               (undefined8 *param_1,byte *param_2,undefined4 param_3)

{
  long *plVar1;
  undefined8 uVar2;
  
                    /* catch() { ... } // from try @ 00b5f94c with catch @ 00b5fdd0 */
                    /* catch() { ... } // from try @ 00b5fa90 with catch @ 00b5fddc */
                    /* catch() { ... } // from try @ 00b5fc00 with catch @ 00b5fde0 */
  param_1 = (undefined8 *)*param_1;
                    /* catch() { ... } // from try @ 00b5fd50 with catch @ 00b5fde8
                       catch() { ... } // from try @ 00b5fd84 with catch @ 00b5fde8 */
  if ((*param_2 & 1) == 0) {
    param_2 = param_2 + 1;
  }
  else {
    param_2 = *(byte **)(param_2 + 0x10);
  }
  plVar1 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
                    /* catch() { ... } // from try @ 00b5fcfc with catch @ 00b5fe08 */
                    /* catch() { ... } // from try @ 00b5f8c0 with catch @ 00b5fe0c */
                    /* catch() { ... } // from try @ 00b5f880 with catch @ 00b5fe10 */
  uVar2 = (**(code **)(*plVar1 + 0x538))(plVar1,param_2);
                    /* catch() { ... } // from try @ 00b5fd18 with catch @ 00b5fe14
                       catch() { ... } // from try @ 00b5fd6c with catch @ 00b5fe14 */
                    /* catch() { ... } // from try @ 00b5f9dc with catch @ 00b5fe1c */
  FUN_00551e14(plVar1,param_1[0x3f],DAT_010a1380,uVar2,param_3);
  (**(code **)(*plVar1 + 0xb8))(plVar1,uVar2);
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5fdcc"></a> `00b5fdcc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b5fdd0"></a> `00b5fdd0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5fdd4"></a> `00b5fdd4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5fdd8"></a> `00b5fdd8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b5fddc"></a> `00b5fddc` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00b5fde0"></a> `00b5fde0` | `16 00 40 f9` | ldr x22,[x0] | `FALL_THROUGH`
<a id="insn-00b5fde4"></a> `00b5fde4` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00b5fde8"></a> `00b5fde8` | `68 00 00 37` | tbnz w8,#0x0,0x00b5fdf4 | `CONDITIONAL_JUMP`
<a id="insn-00b5fdec"></a> `00b5fdec` | `34 04 00 91` | add x20,x1,#0x1 | `FALL_THROUGH`
<a id="insn-00b5fdf0"></a> `00b5fdf0` | `02 00 00 14` | b 0x00b5fdf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5fdf4"></a> `00b5fdf4` | `34 08 40 f9` | ldr x20,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00b5fdf8"></a> `00b5fdf8` | `c0 02 40 f9` | ldr x0,[x22] | `FALL_THROUGH`
<a id="insn-00b5fdfc"></a> `00b5fdfc` | `c1 f8 01 94` | bl 0x00bde100 | `UNCONDITIONAL_CALL`
<a id="insn-00b5fe00"></a> `00b5fe00` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5fe04"></a> `00b5fe04` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b5fe08"></a> `00b5fe08` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b5fe0c"></a> `00b5fe0c` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00b5fe10"></a> `00b5fe10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5fe14"></a> `00b5fe14` | `08 2a 00 d0` | adrp x8,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5fe18"></a> `00b5fe18` | `c1 fe 40 f9` | ldr x1,[x22, #0x1f8] | `FALL_THROUGH`
<a id="insn-00b5fe1c"></a> `00b5fe1c` | `02 c1 41 f9` | ldr x2,[x8, #0x380] | `FALL_THROUGH`
<a id="insn-00b5fe20"></a> `00b5fe20` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b5fe24"></a> `00b5fe24` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b5fe28"></a> `00b5fe28` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00b5fe2c"></a> `00b5fe2c` | `e4 03 13 2a` | mov w4,w19 | `FALL_THROUGH`
<a id="insn-00b5fe30"></a> `00b5fe30` | `f9 c7 e7 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00b5fe34"></a> `00b5fe34` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b5fe38"></a> `00b5fe38` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b5fe3c"></a> `00b5fe3c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b5fe40"></a> `00b5fe40` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00b5fe44"></a> `00b5fe44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5fe48"></a> `00b5fe48` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5fe4c"></a> `00b5fe4c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5fe50"></a> `00b5fe50` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b5fe54"></a> `00b5fe54` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b5fe58"></a> `00b5fe58` | `62 f8 01 14` | b 0x00bddfe0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5fdcc`](#insn-00b5fdcc) 範囲 `[['00b5fdcc', '00b5fdcf']]`
  - `FALL_THROUGH` [`00b5fdcc`](#insn-00b5fdcc) → [`00b5fdd0`](#insn-00b5fdd0)
- ブロック [`00b5fdd0`](#insn-00b5fdd0) 範囲 `[['00b5fdd0', '00b5fddb']]`
  - `FALL_THROUGH` [`00b5fdd8`](#insn-00b5fdd8) → [`00b5fddc`](#insn-00b5fddc)
- ブロック [`00b5fddc`](#insn-00b5fddc) 範囲 `[['00b5fddc', '00b5fddf']]`
  - `FALL_THROUGH` [`00b5fddc`](#insn-00b5fddc) → [`00b5fde0`](#insn-00b5fde0)
- ブロック [`00b5fde0`](#insn-00b5fde0) 範囲 `[['00b5fde0', '00b5fde7']]`
  - `FALL_THROUGH` [`00b5fde4`](#insn-00b5fde4) → [`00b5fde8`](#insn-00b5fde8)
- ブロック [`00b5fde8`](#insn-00b5fde8) 範囲 `[['00b5fde8', '00b5fdeb']]`
  - `CONDITIONAL_JUMP` [`00b5fde8`](#insn-00b5fde8) → [`00b5fdf4`](#insn-00b5fdf4)
  - `FALL_THROUGH` [`00b5fde8`](#insn-00b5fde8) → [`00b5fdec`](#insn-00b5fdec)
- ブロック [`00b5fdec`](#insn-00b5fdec) 範囲 `[['00b5fdec', '00b5fdf3']]`
  - `UNCONDITIONAL_JUMP` [`00b5fdf0`](#insn-00b5fdf0) → [`00b5fdf8`](#insn-00b5fdf8)
- ブロック [`00b5fdf4`](#insn-00b5fdf4) 範囲 `[['00b5fdf4', '00b5fdf7']]`
  - `FALL_THROUGH` [`00b5fdf4`](#insn-00b5fdf4) → [`00b5fdf8`](#insn-00b5fdf8)
- ブロック [`00b5fdf8`](#insn-00b5fdf8) 範囲 `[['00b5fdf8', '00b5fe07']]`
  - `FALL_THROUGH` [`00b5fe04`](#insn-00b5fe04) → [`00b5fe08`](#insn-00b5fe08)
- ブロック [`00b5fe08`](#insn-00b5fe08) 範囲 `[['00b5fe08', '00b5fe0b']]`
  - `FALL_THROUGH` [`00b5fe08`](#insn-00b5fe08) → [`00b5fe0c`](#insn-00b5fe0c)
- ブロック [`00b5fe0c`](#insn-00b5fe0c) 範囲 `[['00b5fe0c', '00b5fe0f']]`
  - `FALL_THROUGH` [`00b5fe0c`](#insn-00b5fe0c) → [`00b5fe10`](#insn-00b5fe10)
- ブロック [`00b5fe10`](#insn-00b5fe10) 範囲 `[['00b5fe10', '00b5fe13']]`
  - `FALL_THROUGH` [`00b5fe10`](#insn-00b5fe10) → [`00b5fe14`](#insn-00b5fe14)
- ブロック [`00b5fe14`](#insn-00b5fe14) 範囲 `[['00b5fe14', '00b5fe1b']]`
  - `FALL_THROUGH` [`00b5fe18`](#insn-00b5fe18) → [`00b5fe1c`](#insn-00b5fe1c)
- ブロック [`00b5fe1c`](#insn-00b5fe1c) 範囲 `[['00b5fe1c', '00b5fe5b']]`

## 命令位置別の参照

- [`00b5fdcc`](#insn-00b5fdcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fdd0`](#insn-00b5fdd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fdd4`](#insn-00b5fdd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fde8`](#insn-00b5fde8) → [`00b5fdf4`](#insn-00b5fdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fdf0`](#insn-00b5fdf0) → [`00b5fdf8`](#insn-00b5fdf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fdfc`](#insn-00b5fdfc) → [`00bde100`](../00bde/00bde100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde100` · 推定シンボル `None` · 推定型 `None`
- [`00b5fe1c`](#insn-00b5fe1c) → `010a1380`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5fe30`](#insn-00b5fe30) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00b5fe48`](#insn-00b5fe48) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fe4c`](#insn-00b5fe4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5fe58`](#insn-00b5fe58) → [`00bddfe0`](../00bdd/00bddfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfe0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5fdcc`](#insn-00b5fdcc)

~~~json
{
  "source": "00b5fdcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fdd0`](#insn-00b5fdd0)

~~~json
{
  "source": "00b5fdd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fdd4`](#insn-00b5fdd4)

~~~json
{
  "source": "00b5fdd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fde8`](#insn-00b5fde8)

~~~json
{
  "source": "00b5fde8",
  "target": "00b5fdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fdf0`](#insn-00b5fdf0)

~~~json
{
  "source": "00b5fdf0",
  "target": "00b5fdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fdfc`](#insn-00b5fdfc)

~~~json
{
  "source": "00b5fdfc",
  "target": "00bde100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5fe1c`](#insn-00b5fe1c)

~~~json
{
  "source": "00b5fe1c",
  "target": "010a1380",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1380",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5fe30`](#insn-00b5fe30)

~~~json
{
  "source": "00b5fe30",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5fe48`](#insn-00b5fe48)

~~~json
{
  "source": "00b5fe48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fe4c`](#insn-00b5fe4c)

~~~json
{
  "source": "00b5fe4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5fe58`](#insn-00b5fe58)

~~~json
{
  "source": "00b5fe58",
  "target": "00bddfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
