# 00ae8cec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae8ca8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8ca8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0063.md#compare-e31720930a18abf3bfceb06ed298f83a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b48a70`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b48/00b48a70.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0015.md#compare-10c65b99216541e605db1cd7c31598ea)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae8cec",
  "name": "_ZN8firebase4util11class_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42bf2ab47f908db1f4662a80212e5e865e0516931f5788c3868db17a1533c17d",
  "source_text_sha256": "42bf2ab47f908db1f4662a80212e5e865e0516931f5788c3868db17a1533c17d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae8cec",
        "00ae8d87"
      ]
    ],
    "bytes_sha256": "24b16e76c37d9b14af1952fe2dc9424cf74bf62d27f3dd0f39e8162ef41a0f87",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1477 bytes

~~~c

bool _ZN8firebase4util11class_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
                    /* catch() { ... } // from try @ 00ae7568 with catch @ 00ae8cec */
                    /* catch() { ... } // from try @ 00ae753c with catch @ 00ae8d04 */
  if (DAT_010a06a0 == '\0') {
                    /* catch() { ... } // from try @ 00ae7528 with catch @ 00ae8d1c */
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a0698,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
                    /* catch() { ... } // from try @ 00ae7518 with catch @ 00ae8d4c */
      (**(code **)(*param_1 + 0x80))(param_1);
                    /* catch() { ... } // from try @ 00ae74e0 with catch @ 00ae8d60 */
                    /* catch() { ... } // from try @ 00ae7944 with catch @ 00ae8d64 */
                    /* catch() { ... } // from try @ 00ae7020 with catch @ 00ae8d68 */
      (**(code **)(*param_1 + 0x88))(param_1);
    }
                    /* catch() { ... } // from try @ 00ae6084 with catch @ 00ae8d6c */
    DAT_010a06a0 = iVar3 == 0;
                    /* catch() { ... } // from try @ 00ae8148 with catch @ 00ae8d70
                       catch() { ... } // from try @ 00ae86ac with catch @ 00ae8d70 */
    bVar2 = (bool)DAT_010a06a0;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae8cec"></a> `00ae8cec` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ae8cf0"></a> `00ae8cf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae8cf4"></a> `00ae8cf4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae8cf8"></a> `00ae8cf8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ae8cfc"></a> `00ae8cfc` | `d5 2d 00 90` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae8d00"></a> `00ae8d00` | `a8 82 5a 39` | ldrb w8,[x21, #0x6a0] | `FALL_THROUGH`
<a id="insn-00ae8d04"></a> `00ae8d04` | `68 00 00 34` | cbz w8,0x00ae8d10 | `CONDITIONAL_JUMP`
<a id="insn-00ae8d08"></a> `00ae8d08` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ae8d0c"></a> `00ae8d0c` | `1b 00 00 14` | b 0x00ae8d78 | `UNCONDITIONAL_JUMP`
<a id="insn-00ae8d10"></a> `00ae8d10` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ae8d14"></a> `00ae8d14` | `c9 2d 00 90` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae8d18"></a> `00ae8d18` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00ae8d1c"></a> `00ae8d1c` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00ae8d20"></a> `00ae8d20` | `21 4d 43 f9` | ldr x1,[x9, #0x698] | `FALL_THROUGH`
<a id="insn-00ae8d24"></a> `00ae8d24` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00ae8d28"></a> `00ae8d28` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae8d2c"></a> `00ae8d2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae8d30"></a> `00ae8d30` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae8d34"></a> `00ae8d34` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00ae8d38"></a> `00ae8d38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae8d3c"></a> `00ae8d3c` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00ae8d40"></a> `00ae8d40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae8d44"></a> `00ae8d44` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00ae8d48"></a> `00ae8d48` | `20 01 00 54` | b.eq 0x00ae8d6c | `CONDITIONAL_JUMP`
<a id="insn-00ae8d4c"></a> `00ae8d4c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae8d50"></a> `00ae8d50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae8d54"></a> `00ae8d54` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00ae8d58"></a> `00ae8d58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae8d5c"></a> `00ae8d5c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae8d60"></a> `00ae8d60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae8d64"></a> `00ae8d64` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00ae8d68"></a> `00ae8d68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae8d6c"></a> `00ae8d6c` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00ae8d70"></a> `00ae8d70` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00ae8d74"></a> `00ae8d74` | `a0 82 1a 39` | strb w0,[x21, #0x6a0] | `FALL_THROUGH`
<a id="insn-00ae8d78"></a> `00ae8d78` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae8d7c"></a> `00ae8d7c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae8d80"></a> `00ae8d80` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ae8d84"></a> `00ae8d84` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae8cec`](#insn-00ae8cec) 範囲 `[['00ae8cec', '00ae8d03']]`
  - `FALL_THROUGH` [`00ae8d00`](#insn-00ae8d00) → [`00ae8d04`](#insn-00ae8d04)
- ブロック [`00ae8d04`](#insn-00ae8d04) 範囲 `[['00ae8d04', '00ae8d07']]`
  - `CONDITIONAL_JUMP` [`00ae8d04`](#insn-00ae8d04) → [`00ae8d10`](#insn-00ae8d10)
  - `FALL_THROUGH` [`00ae8d04`](#insn-00ae8d04) → [`00ae8d08`](#insn-00ae8d08)
- ブロック [`00ae8d08`](#insn-00ae8d08) 範囲 `[['00ae8d08', '00ae8d0f']]`
  - `UNCONDITIONAL_JUMP` [`00ae8d0c`](#insn-00ae8d0c) → [`00ae8d78`](#insn-00ae8d78)
- ブロック [`00ae8d10`](#insn-00ae8d10) 範囲 `[['00ae8d10', '00ae8d1b']]`
  - `FALL_THROUGH` [`00ae8d18`](#insn-00ae8d18) → [`00ae8d1c`](#insn-00ae8d1c)
- ブロック [`00ae8d1c`](#insn-00ae8d1c) 範囲 `[['00ae8d1c', '00ae8d4b']]`
  - `CONDITIONAL_JUMP` [`00ae8d48`](#insn-00ae8d48) → [`00ae8d6c`](#insn-00ae8d6c)
  - `FALL_THROUGH` [`00ae8d48`](#insn-00ae8d48) → [`00ae8d4c`](#insn-00ae8d4c)
- ブロック [`00ae8d4c`](#insn-00ae8d4c) 範囲 `[['00ae8d4c', '00ae8d5f']]`
  - `FALL_THROUGH` [`00ae8d5c`](#insn-00ae8d5c) → [`00ae8d60`](#insn-00ae8d60)
- ブロック [`00ae8d60`](#insn-00ae8d60) 範囲 `[['00ae8d60', '00ae8d63']]`
  - `FALL_THROUGH` [`00ae8d60`](#insn-00ae8d60) → [`00ae8d64`](#insn-00ae8d64)
- ブロック [`00ae8d64`](#insn-00ae8d64) 範囲 `[['00ae8d64', '00ae8d67']]`
  - `FALL_THROUGH` [`00ae8d64`](#insn-00ae8d64) → [`00ae8d68`](#insn-00ae8d68)
- ブロック [`00ae8d68`](#insn-00ae8d68) 範囲 `[['00ae8d68', '00ae8d6b']]`
  - `FALL_THROUGH` [`00ae8d68`](#insn-00ae8d68) → [`00ae8d6c`](#insn-00ae8d6c)
- ブロック [`00ae8d6c`](#insn-00ae8d6c) 範囲 `[['00ae8d6c', '00ae8d6f']]`
  - `FALL_THROUGH` [`00ae8d6c`](#insn-00ae8d6c) → [`00ae8d70`](#insn-00ae8d70)
- ブロック [`00ae8d70`](#insn-00ae8d70) 範囲 `[['00ae8d70', '00ae8d77']]`
  - `FALL_THROUGH` [`00ae8d74`](#insn-00ae8d74) → [`00ae8d78`](#insn-00ae8d78)
- ブロック [`00ae8d78`](#insn-00ae8d78) 範囲 `[['00ae8d78', '00ae8d87']]`

## 命令位置別の参照

- [`00ae8cec`](#insn-00ae8cec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8cf0`](#insn-00ae8cf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8cf4`](#insn-00ae8cf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8d00`](#insn-00ae8d00) → `010a06a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae8d04`](#insn-00ae8d04) → [`00ae8d10`](#insn-00ae8d10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8d0c`](#insn-00ae8d0c) → [`00ae8d78`](#insn-00ae8d78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8d20`](#insn-00ae8d20) → `010a0698`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae8d48`](#insn-00ae8d48) → [`00ae8d6c`](#insn-00ae8d6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8d74`](#insn-00ae8d74) → `010a06a0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae8d78`](#insn-00ae8d78) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8d7c`](#insn-00ae8d7c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae8cec`](#insn-00ae8cec)

~~~json
{
  "source": "00ae8cec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8cf0`](#insn-00ae8cf0)

~~~json
{
  "source": "00ae8cf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8cf4`](#insn-00ae8cf4)

~~~json
{
  "source": "00ae8cf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8d00`](#insn-00ae8d00)

~~~json
{
  "source": "00ae8d00",
  "target": "010a06a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a06a0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae8d04`](#insn-00ae8d04)

~~~json
{
  "source": "00ae8d04",
  "target": "00ae8d10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8d0c`](#insn-00ae8d0c)

~~~json
{
  "source": "00ae8d0c",
  "target": "00ae8d78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8d20`](#insn-00ae8d20)

~~~json
{
  "source": "00ae8d20",
  "target": "010a0698",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0698",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae8d48`](#insn-00ae8d48)

~~~json
{
  "source": "00ae8d48",
  "target": "00ae8d6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8d74`](#insn-00ae8d74)

~~~json
{
  "source": "00ae8d74",
  "target": "010a06a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a06a0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae8d78`](#insn-00ae8d78)

~~~json
{
  "source": "00ae8d78",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8d7c`](#insn-00ae8d7c)

~~~json
{
  "source": "00ae8d7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
