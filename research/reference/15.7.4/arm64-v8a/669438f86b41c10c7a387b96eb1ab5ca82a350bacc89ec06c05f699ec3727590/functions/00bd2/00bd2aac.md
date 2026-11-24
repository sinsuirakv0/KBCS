# 00bd2aac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bd2a68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd2/00bd2a68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0019.md#compare-80adf62eb0225b1504e4150839c982b0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c4f4f4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f4f4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0020.md#compare-426eb77f81a97829d04d51e1195da7ed)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd2aac",
  "name": "FUN_00bd2aac",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "705bb0285fc4a5f3b8edddbef23a514b224b604afb59771c6b4c8c9d189609cb",
  "source_text_sha256": "705bb0285fc4a5f3b8edddbef23a514b224b604afb59771c6b4c8c9d189609cb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd2aac",
        "00bd2b2f"
      ]
    ],
    "bytes_sha256": "4e619d399d6701f73c9719caa09eaa510adc6bdf3a8643caab0803ac433734de",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1404 bytes

~~~c

void FUN_00bd2aac(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *__ptr;
  long lVar2;
  size_t __size;
  
  (**(code **)(**(long **)(param_1 + 0x10) + 0x20))();
  lVar2 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 1U) {
                    /* catch() { ... } // from try @ 00bd2090 with catch @ 00bd2ae4 */
    __size = param_2[2] * 2;
                    /* catch() { ... } // from try @ 00bd1de8 with catch @ 00bd2ae8 */
    uVar1 = lVar2 + 0x3e1;
                    /* catch() { ... } // from try @ 00bd232c with catch @ 00bd2aec */
                    /* catch() { ... } // from try @ 00bd2300 with catch @ 00bd2af0
                       catch() { ... } // from try @ 00bd2850 with catch @ 00bd2af0 */
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
                    /* catch() { ... } // from try @ 00bd2180 with catch @ 00bd2af8 */
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
  }
  *(undefined1 *)((long)__ptr + lVar2) = 0x20;
                    /* catch() { ... } // from try @ 00bd2138 with catch @ 00bd2b10
                       catch() { ... } // from try @ 00bd2834 with catch @ 00bd2b10 */
  param_2[1] = param_2[1] + 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd2aac"></a> `00bd2aac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd2ab0"></a> `00bd2ab0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd2ab4"></a> `00bd2ab4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2ab8"></a> `00bd2ab8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd2abc"></a> `00bd2abc` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2ac0"></a> `00bd2ac0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bd2ac4"></a> `00bd2ac4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd2ac8"></a> `00bd2ac8` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bd2acc"></a> `00bd2acc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd2ad0"></a> `00bd2ad0` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2ad4"></a> `00bd2ad4` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2ad8"></a> `00bd2ad8` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2adc"></a> `00bd2adc` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd2ae0"></a> `00bd2ae0` | `49 01 00 54` | b.ls 0x00bd2b08 | `CONDITIONAL_JUMP`
<a id="insn-00bd2ae4"></a> `00bd2ae4` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2ae8"></a> `00bd2ae8` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bd2aec"></a> `00bd2aec` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd2af0"></a> `00bd2af0` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd2af4"></a> `00bd2af4` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2af8"></a> `00bd2af8` | `d6 29 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2afc"></a> `00bd2afc` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd2b00"></a> `00bd2b00` | `60 01 00 b4` | cbz x0,0x00bd2b2c | `CONDITIONAL_JUMP`
<a id="insn-00bd2b04"></a> `00bd2b04` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2b08"></a> `00bd2b08` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bd2b0c"></a> `00bd2b0c` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bd2b10"></a> `00bd2b10` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2b14"></a> `00bd2b14` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2b18"></a> `00bd2b18` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2b1c"></a> `00bd2b1c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2b20"></a> `00bd2b20` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd2b24"></a> `00bd2b24` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd2b28"></a> `00bd2b28` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd2b2c"></a> `00bd2b2c` | `e5 2d 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd2aac`](#insn-00bd2aac) 範囲 `[['00bd2aac', '00bd2ae3']]`
  - `CONDITIONAL_JUMP` [`00bd2ae0`](#insn-00bd2ae0) → [`00bd2b08`](#insn-00bd2b08)
  - `FALL_THROUGH` [`00bd2ae0`](#insn-00bd2ae0) → [`00bd2ae4`](#insn-00bd2ae4)
- ブロック [`00bd2ae4`](#insn-00bd2ae4) 範囲 `[['00bd2ae4', '00bd2ae7']]`
  - `FALL_THROUGH` [`00bd2ae4`](#insn-00bd2ae4) → [`00bd2ae8`](#insn-00bd2ae8)
- ブロック [`00bd2ae8`](#insn-00bd2ae8) 範囲 `[['00bd2ae8', '00bd2aeb']]`
  - `FALL_THROUGH` [`00bd2ae8`](#insn-00bd2ae8) → [`00bd2aec`](#insn-00bd2aec)
- ブロック [`00bd2aec`](#insn-00bd2aec) 範囲 `[['00bd2aec', '00bd2aef']]`
  - `FALL_THROUGH` [`00bd2aec`](#insn-00bd2aec) → [`00bd2af0`](#insn-00bd2af0)
- ブロック [`00bd2af0`](#insn-00bd2af0) 範囲 `[['00bd2af0', '00bd2af7']]`
  - `FALL_THROUGH` [`00bd2af4`](#insn-00bd2af4) → [`00bd2af8`](#insn-00bd2af8)
- ブロック [`00bd2af8`](#insn-00bd2af8) 範囲 `[['00bd2af8', '00bd2b03']]`
  - `CONDITIONAL_JUMP` [`00bd2b00`](#insn-00bd2b00) → [`00bd2b2c`](#insn-00bd2b2c)
  - `FALL_THROUGH` [`00bd2b00`](#insn-00bd2b00) → [`00bd2b04`](#insn-00bd2b04)
- ブロック [`00bd2b04`](#insn-00bd2b04) 範囲 `[['00bd2b04', '00bd2b07']]`
  - `FALL_THROUGH` [`00bd2b04`](#insn-00bd2b04) → [`00bd2b08`](#insn-00bd2b08)
- ブロック [`00bd2b08`](#insn-00bd2b08) 範囲 `[['00bd2b08', '00bd2b0f']]`
  - `FALL_THROUGH` [`00bd2b0c`](#insn-00bd2b0c) → [`00bd2b10`](#insn-00bd2b10)
- ブロック [`00bd2b10`](#insn-00bd2b10) 範囲 `[['00bd2b10', '00bd2b2b']]`
- ブロック [`00bd2b2c`](#insn-00bd2b2c) 範囲 `[['00bd2b2c', '00bd2b2f']]`

## 命令位置別の参照

- [`00bd2ab0`](#insn-00bd2ab0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ab4`](#insn-00bd2ab4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2ae0`](#insn-00bd2ae0) → [`00bd2b08`](#insn-00bd2b08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2af8`](#insn-00bd2af8) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bd2b00`](#insn-00bd2b00) → [`00bd2b2c`](#insn-00bd2b2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2b1c`](#insn-00bd2b1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2b20`](#insn-00bd2b20) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2b2c`](#insn-00bd2b2c) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd2ab0`](#insn-00bd2ab0)

~~~json
{
  "source": "00bd2ab0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2ab4`](#insn-00bd2ab4)

~~~json
{
  "source": "00bd2ab4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2ae0`](#insn-00bd2ae0)

~~~json
{
  "source": "00bd2ae0",
  "target": "00bd2b08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2af8`](#insn-00bd2af8)

~~~json
{
  "source": "00bd2af8",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2b00`](#insn-00bd2b00)

~~~json
{
  "source": "00bd2b00",
  "target": "00bd2b2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2b1c`](#insn-00bd2b1c)

~~~json
{
  "source": "00bd2b1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2b20`](#insn-00bd2b20)

~~~json
{
  "source": "00bd2b20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2b2c`](#insn-00bd2b2c)

~~~json
{
  "source": "00bd2b2c",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
