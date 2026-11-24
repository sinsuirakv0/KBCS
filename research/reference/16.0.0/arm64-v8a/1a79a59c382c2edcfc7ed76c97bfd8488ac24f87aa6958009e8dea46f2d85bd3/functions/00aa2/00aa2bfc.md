# 00aa2bfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a44cf8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44cf8.md) · 移動量 `+0x5df04`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-f95e4cdda8a54129821c04de11551ea3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aa2df8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa2/00aa2df8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-44597d30388ecef29ab0c35fa1da5148)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa2bfc",
  "name": "FUN_00aa2bfc",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e269cb7a9155463c7f64c3a6ea6843bdf42c2a946ca918575ff6bca744eb2bcb",
  "source_text_sha256": "e269cb7a9155463c7f64c3a6ea6843bdf42c2a946ca918575ff6bca744eb2bcb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa2bfc",
        "00aa2c77"
      ]
    ],
    "bytes_sha256": "d659298843764c8b9de3c61f9fe7b0afd98ab725af7d71e1bcf99b97face7437",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005fe62c](../005fe/005fe62c.md)
- [007bda04](../007bd/007bda04.md)
- [007cceac](../007cc/007cceac.md)
- [007df0a8](../007df/007df0a8.md)

## 呼び出し先

- [004428f0](../00442/004428f0.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 969 bytes

~~~c

undefined4 FUN_00aa2bfc(long param_1,int param_2)

{
  long *plVar1;
  long *plVar2;
  
  plVar1 = *(long **)(param_1 + 0x20);
  plVar2 = plVar1;
  do {
    if (plVar2 == (long *)0x0) {
      return 0;
    }
    if (*(int *)((long)plVar2 + 0x1c) <= param_2) {
      if (param_2 <= *(int *)((long)plVar2 + 0x1c)) {
        do {
          if (param_2 < *(int *)((long)plVar1 + 0x1c)) {
            plVar1 = (long *)*plVar1;
          }
          else {
            if (param_2 <= *(int *)((long)plVar1 + 0x1c)) {
                    /* catch() { ... } // from try @ 00aa2f5c with catch @ 00aa2c70 */
              return *(undefined4 *)((long)plVar1 + 0x24);
            }
            plVar1 = (long *)plVar1[1];
          }
        } while (plVar1 != (long *)0x0);
                    /* WARNING: Subroutine does not return */
        FUN_004428f0("map::at:  key not found");
      }
      plVar2 = plVar2 + 1;
    }
    plVar2 = (long *)*plVar2;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa2bfc"></a> `00aa2bfc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00aa2c00"></a> `00aa2c00` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aa2c04"></a> `00aa2c04` | `08 10 40 f9` | ldr x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aa2c08"></a> `00aa2c08` | `c8 02 00 b4` | cbz x8,0x00aa2c60 | `CONDITIONAL_JUMP`
<a id="insn-00aa2c0c"></a> `00aa2c0c` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00aa2c10"></a> `00aa2c10` | `03 00 00 14` | b 0x00aa2c1c | `UNCONDITIONAL_JUMP`
<a id="insn-00aa2c14"></a> `00aa2c14` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aa2c18"></a> `00aa2c18` | `49 02 00 b4` | cbz x9,0x00aa2c60 | `CONDITIONAL_JUMP`
<a id="insn-00aa2c1c"></a> `00aa2c1c` | `2a 1d 40 b9` | ldr w10,[x9, #0x1c] | `FALL_THROUGH`
<a id="insn-00aa2c20"></a> `00aa2c20` | `5f 01 01 6b` | cmp w10,w1 | `FALL_THROUGH`
<a id="insn-00aa2c24"></a> `00aa2c24` | `8c ff ff 54` | b.gt 0x00aa2c14 | `CONDITIONAL_JUMP`
<a id="insn-00aa2c28"></a> `00aa2c28` | `aa 00 00 54` | b.ge 0x00aa2c3c | `CONDITIONAL_JUMP`
<a id="insn-00aa2c2c"></a> `00aa2c2c` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00aa2c30"></a> `00aa2c30` | `f9 ff ff 17` | b 0x00aa2c14 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa2c34"></a> `00aa2c34` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aa2c38"></a> `00aa2c38` | `e8 00 00 b4` | cbz x8,0x00aa2c54 | `CONDITIONAL_JUMP`
<a id="insn-00aa2c3c"></a> `00aa2c3c` | `09 1d 40 b9` | ldr w9,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aa2c40"></a> `00aa2c40` | `3f 01 01 6b` | cmp w9,w1 | `FALL_THROUGH`
<a id="insn-00aa2c44"></a> `00aa2c44` | `8c ff ff 54` | b.gt 0x00aa2c34 | `CONDITIONAL_JUMP`
<a id="insn-00aa2c48"></a> `00aa2c48` | `2a 01 00 54` | b.ge 0x00aa2c6c | `CONDITIONAL_JUMP`
<a id="insn-00aa2c4c"></a> `00aa2c4c` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00aa2c50"></a> `00aa2c50` | `68 ff ff b5` | cbnz x8,0x00aa2c3c | `CONDITIONAL_JUMP`
<a id="insn-00aa2c54"></a> `00aa2c54` | `e0 bf ff d0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00aa2c58"></a> `00aa2c58` | `00 c0 03 91` | add x0,x0,#0xf0 | `FALL_THROUGH`
<a id="insn-00aa2c5c"></a> `00aa2c5c` | `25 7f e6 97` | bl 0x004428f0 | `CALL_TERMINATOR`
<a id="insn-00aa2c60"></a> `00aa2c60` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aa2c64"></a> `00aa2c64` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00aa2c68"></a> `00aa2c68` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa2c6c"></a> `00aa2c6c` | `00 25 40 b9` | ldr w0,[x8, #0x24] | `FALL_THROUGH`
<a id="insn-00aa2c70"></a> `00aa2c70` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00aa2c74"></a> `00aa2c74` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa2bfc`](#insn-00aa2bfc) 範囲 `[['00aa2bfc', '00aa2c0b']]`
  - `CONDITIONAL_JUMP` [`00aa2c08`](#insn-00aa2c08) → [`00aa2c60`](#insn-00aa2c60)
  - `FALL_THROUGH` [`00aa2c08`](#insn-00aa2c08) → [`00aa2c0c`](#insn-00aa2c0c)
- ブロック [`00aa2c0c`](#insn-00aa2c0c) 範囲 `[['00aa2c0c', '00aa2c13']]`
  - `UNCONDITIONAL_JUMP` [`00aa2c10`](#insn-00aa2c10) → [`00aa2c1c`](#insn-00aa2c1c)
- ブロック [`00aa2c14`](#insn-00aa2c14) 範囲 `[['00aa2c14', '00aa2c1b']]`
  - `CONDITIONAL_JUMP` [`00aa2c18`](#insn-00aa2c18) → [`00aa2c60`](#insn-00aa2c60)
  - `FALL_THROUGH` [`00aa2c18`](#insn-00aa2c18) → [`00aa2c1c`](#insn-00aa2c1c)
- ブロック [`00aa2c1c`](#insn-00aa2c1c) 範囲 `[['00aa2c1c', '00aa2c27']]`
  - `CONDITIONAL_JUMP` [`00aa2c24`](#insn-00aa2c24) → [`00aa2c14`](#insn-00aa2c14)
  - `FALL_THROUGH` [`00aa2c24`](#insn-00aa2c24) → [`00aa2c28`](#insn-00aa2c28)
- ブロック [`00aa2c28`](#insn-00aa2c28) 範囲 `[['00aa2c28', '00aa2c2b']]`
  - `CONDITIONAL_JUMP` [`00aa2c28`](#insn-00aa2c28) → [`00aa2c3c`](#insn-00aa2c3c)
  - `FALL_THROUGH` [`00aa2c28`](#insn-00aa2c28) → [`00aa2c2c`](#insn-00aa2c2c)
- ブロック [`00aa2c2c`](#insn-00aa2c2c) 範囲 `[['00aa2c2c', '00aa2c33']]`
  - `UNCONDITIONAL_JUMP` [`00aa2c30`](#insn-00aa2c30) → [`00aa2c14`](#insn-00aa2c14)
- ブロック [`00aa2c34`](#insn-00aa2c34) 範囲 `[['00aa2c34', '00aa2c3b']]`
  - `CONDITIONAL_JUMP` [`00aa2c38`](#insn-00aa2c38) → [`00aa2c54`](#insn-00aa2c54)
  - `FALL_THROUGH` [`00aa2c38`](#insn-00aa2c38) → [`00aa2c3c`](#insn-00aa2c3c)
- ブロック [`00aa2c3c`](#insn-00aa2c3c) 範囲 `[['00aa2c3c', '00aa2c47']]`
  - `CONDITIONAL_JUMP` [`00aa2c44`](#insn-00aa2c44) → [`00aa2c34`](#insn-00aa2c34)
  - `FALL_THROUGH` [`00aa2c44`](#insn-00aa2c44) → [`00aa2c48`](#insn-00aa2c48)
- ブロック [`00aa2c48`](#insn-00aa2c48) 範囲 `[['00aa2c48', '00aa2c4b']]`
  - `CONDITIONAL_JUMP` [`00aa2c48`](#insn-00aa2c48) → [`00aa2c6c`](#insn-00aa2c6c)
  - `FALL_THROUGH` [`00aa2c48`](#insn-00aa2c48) → [`00aa2c4c`](#insn-00aa2c4c)
- ブロック [`00aa2c4c`](#insn-00aa2c4c) 範囲 `[['00aa2c4c', '00aa2c53']]`
  - `CONDITIONAL_JUMP` [`00aa2c50`](#insn-00aa2c50) → [`00aa2c3c`](#insn-00aa2c3c)
  - `FALL_THROUGH` [`00aa2c50`](#insn-00aa2c50) → [`00aa2c54`](#insn-00aa2c54)
- ブロック [`00aa2c54`](#insn-00aa2c54) 範囲 `[['00aa2c54', '00aa2c5f']]`
- ブロック [`00aa2c60`](#insn-00aa2c60) 範囲 `[['00aa2c60', '00aa2c6b']]`
- ブロック [`00aa2c6c`](#insn-00aa2c6c) 範囲 `[['00aa2c6c', '00aa2c6f']]`
  - `FALL_THROUGH` [`00aa2c6c`](#insn-00aa2c6c) → [`00aa2c70`](#insn-00aa2c70)
- ブロック [`00aa2c70`](#insn-00aa2c70) 範囲 `[['00aa2c70', '00aa2c77']]`

## 命令位置別の参照

- [`00aa2bfc`](#insn-00aa2bfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c08`](#insn-00aa2c08) → [`00aa2c60`](#insn-00aa2c60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c10`](#insn-00aa2c10) → [`00aa2c1c`](#insn-00aa2c1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c18`](#insn-00aa2c18) → [`00aa2c60`](#insn-00aa2c60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c24`](#insn-00aa2c24) → [`00aa2c14`](#insn-00aa2c14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c28`](#insn-00aa2c28) → [`00aa2c3c`](#insn-00aa2c3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c30`](#insn-00aa2c30) → [`00aa2c14`](#insn-00aa2c14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c38`](#insn-00aa2c38) → [`00aa2c54`](#insn-00aa2c54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c44`](#insn-00aa2c44) → [`00aa2c34`](#insn-00aa2c34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c48`](#insn-00aa2c48) → [`00aa2c6c`](#insn-00aa2c6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c50`](#insn-00aa2c50) → [`00aa2c3c`](#insn-00aa2c3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c58`](#insn-00aa2c58) → `002a00f0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aa2c5c`](#insn-00aa2c5c) → [`004428f0`](../00442/004428f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004428f0` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c64`](#insn-00aa2c64) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa2c70`](#insn-00aa2c70) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa2bfc`](#insn-00aa2bfc)

~~~json
{
  "source": "00aa2bfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c08`](#insn-00aa2c08)

~~~json
{
  "source": "00aa2c08",
  "target": "00aa2c60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c10`](#insn-00aa2c10)

~~~json
{
  "source": "00aa2c10",
  "target": "00aa2c1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c18`](#insn-00aa2c18)

~~~json
{
  "source": "00aa2c18",
  "target": "00aa2c60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c24`](#insn-00aa2c24)

~~~json
{
  "source": "00aa2c24",
  "target": "00aa2c14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c28`](#insn-00aa2c28)

~~~json
{
  "source": "00aa2c28",
  "target": "00aa2c3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c30`](#insn-00aa2c30)

~~~json
{
  "source": "00aa2c30",
  "target": "00aa2c14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c38`](#insn-00aa2c38)

~~~json
{
  "source": "00aa2c38",
  "target": "00aa2c54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c44`](#insn-00aa2c44)

~~~json
{
  "source": "00aa2c44",
  "target": "00aa2c34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c48`](#insn-00aa2c48)

~~~json
{
  "source": "00aa2c48",
  "target": "00aa2c6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c50`](#insn-00aa2c50)

~~~json
{
  "source": "00aa2c50",
  "target": "00aa2c3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c58`](#insn-00aa2c58)

~~~json
{
  "source": "00aa2c58",
  "target": "002a00f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a00f0",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "6d61703a3a61743a20206b6579206e6f7420666f756e6400",
  "capture_start": "002a00f0",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aa2c5c`](#insn-00aa2c5c)

~~~json
{
  "source": "00aa2c5c",
  "target": "004428f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa2c64`](#insn-00aa2c64)

~~~json
{
  "source": "00aa2c64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa2c70`](#insn-00aa2c70)

~~~json
{
  "source": "00aa2c70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
