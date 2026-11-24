# 00bcbce4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c7e4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c7e4.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-43147e795b10430e6f508d751c01f9f1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc10c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc10c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-9e757f7c31a200ff682680ebd2597b42)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbce4",
  "name": "_INIT_290",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "70f5f0aba6fea76c33cc3555caf3ae6f0fe94cb1e7e5f7928edf4eed99919079",
  "source_text_sha256": "70f5f0aba6fea76c33cc3555caf3ae6f0fe94cb1e7e5f7928edf4eed99919079",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbce4",
        "00bcbd77"
      ]
    ],
    "bytes_sha256": "038ace0adbc76f88e288bd05806058d683e5414c08383d04e74b14da1bd91d53",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57a30](../00c57/00c57a30.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c5a7c0](../00c5a/00c5a7c0.md)
- [00c5a880](../00c5a/00c5a880.md)

## 関連文字列（未確認候補）

~~~text
"auth"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 940 bytes

~~~c

void _INIT_290(void)

{
  undefined *puVar1;
  undefined8 uVar2;
  undefined8 *puVar3;
  
  DAT_011262e8 = &DAT_002bc0ca;
  DAT_011262f0 = FUN_00bca0a8;
  DAT_011262f8 = FUN_00bca0b0;
  DAT_01126300 = 0;
  _ZN8firebase11AppCallback11AddCallbackEPS0_();
  puVar1 = PTR__ZN8firebase4auth7g_authsE_00c9b5a8;
                    /* try { // try from 00bcbd30 to 00ccbd8f has its CatchHandler @ 00bcbd30
                       catch() { ... } // from try @ 00bcbd30 with catch @ 00bcbd30
                       catch() { ... } // from try @ 00bcbd9c with catch @ 00bcbd30 */
  puVar3 = (undefined8 *)(PTR__ZN8firebase4auth7g_authsE_00c9b5a8 + 8);
  *puVar3 = 0;
  *(undefined8 *)(puVar1 + 0x10) = 0;
  *(undefined8 **)puVar1 = puVar3;
  __cxa_atexit(FUN_00bca0b4,puVar1,&PTR_LOOP_00c62b90);
  uVar2 = _Znwm(0x28);
  _ZN8firebase5MutexC1ENS0_4ModeE(uVar2,1);
  *(undefined8 *)PTR__ZN8firebase4auth13g_auths_mutexE_00c9b5a0 = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbce4"></a> `00bcbce4` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcbce8"></a> `00bcbce8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbcec"></a> `00bcbcec` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcbcf0"></a> `00bcbcf0` | `c0 2a 00 f0` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcbcf4"></a> `00bcbcf4` | `88 b7 ff b0` | adrp x8,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bcbcf8"></a> `00bcbcf8` | `e9 ff ff f0` | adrp x9,0xbca000 | `FALL_THROUGH`
<a id="insn-00bcbcfc"></a> `00bcbcfc` | `ea ff ff f0` | adrp x10,0xbca000 | `FALL_THROUGH`
<a id="insn-00bcbd00"></a> `00bcbd00` | `00 a0 0b 91` | add x0,x0,#0x2e8 | `FALL_THROUGH`
<a id="insn-00bcbd04"></a> `00bcbd04` | `08 29 03 91` | add x8,x8,#0xca | `FALL_THROUGH`
<a id="insn-00bcbd08"></a> `00bcbd08` | `29 a1 02 91` | add x9,x9,#0xa8 | `FALL_THROUGH`
<a id="insn-00bcbd0c"></a> `00bcbd0c` | `4a c1 02 91` | add x10,x10,#0xb0 | `FALL_THROUGH`
<a id="insn-00bcbd10"></a> `00bcbd10` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bcbd14"></a> `00bcbd14` | `0a 08 00 f9` | str x10,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbd18"></a> `00bcbd18` | `1f 60 00 39` | strb wzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bcbd1c"></a> `00bcbd1c` | `a9 3a 02 94` | bl 0x00c5a7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbd20"></a> `00bcbd20` | `81 06 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcbd24"></a> `00bcbd24` | `21 d4 42 f9` | ldr x1,[x1, #0x5a8] | `FALL_THROUGH`
<a id="insn-00bcbd28"></a> `00bcbd28` | `e0 ff ff f0` | adrp x0,0xbca000 | `FALL_THROUGH`
<a id="insn-00bcbd2c"></a> `00bcbd2c` | `a2 04 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00bcbd30"></a> `00bcbd30` | `00 d0 02 91` | add x0,x0,#0xb4 | `FALL_THROUGH`
<a id="insn-00bcbd34"></a> `00bcbd34` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bcbd38"></a> `00bcbd38` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00bcbd3c"></a> `00bcbd3c` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-00bcbd40"></a> `00bcbd40` | `3f 08 00 f9` | str xzr,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbd44"></a> `00bcbd44` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcbd48"></a> `00bcbd48` | `3a 2f 02 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbd4c"></a> `00bcbd4c` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00bcbd50"></a> `00bcbd50` | `50 2f 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbd54"></a> `00bcbd54` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcbd58"></a> `00bcbd58` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbd5c"></a> `00bcbd5c` | `c9 3a 02 94` | bl 0x00c5a880 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbd60"></a> `00bcbd60` | `88 06 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcbd64"></a> `00bcbd64` | `08 d1 42 f9` | ldr x8,[x8, #0x5a0] | `FALL_THROUGH`
<a id="insn-00bcbd68"></a> `00bcbd68` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbd6c"></a> `00bcbd6c` | `13 01 00 f9` | str x19,[x8] | `FALL_THROUGH`
<a id="insn-00bcbd70"></a> `00bcbd70` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcbd74"></a> `00bcbd74` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbce4`](#insn-00bcbce4) 範囲 `[['00bcbce4', '00bcbd2f']]`
  - `FALL_THROUGH` [`00bcbd2c`](#insn-00bcbd2c) → [`00bcbd30`](#insn-00bcbd30)
- ブロック [`00bcbd30`](#insn-00bcbd30) 範囲 `[['00bcbd30', '00bcbd77']]`

## 命令位置別の参照

- [`00bcbce4`](#insn-00bcbce4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbce8`](#insn-00bcbce8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd00`](#insn-00bcbd00) → `011262e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbd10`](#insn-00bcbd10) → `011262e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbd10`](#insn-00bcbd10) → `002bc0ca`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd10`](#insn-00bcbd10) → `011262f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbd10`](#insn-00bcbd10) → [`00bca0a8`](../00bca/00bca0a8.md) · `DATA` · `ANALYSIS` · 関数 `00bca0a8` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd14`](#insn-00bcbd14) → `011262f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbd14`](#insn-00bcbd14) → [`00bca0b0`](../00bca/00bca0b0.md) · `DATA` · `ANALYSIS` · 関数 `00bca0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd18`](#insn-00bcbd18) → `01126300`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcbd1c`](#insn-00bcbd1c) → [`00c5a7c0`](../00c5a/00c5a7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd24`](#insn-00bcbd24) → `00c9b5a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcbd24`](#insn-00bcbd24) → `01126308`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bcbd30`](#insn-00bcbd30) → [`00bca0b4`](../00bca/00bca0b4.md) · `PARAM` · `ANALYSIS` · 関数 `00bca0b4` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd38`](#insn-00bcbd38) → `01126310`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbd3c`](#insn-00bcbd3c) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcbd40`](#insn-00bcbd40) → `01126318`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbd44`](#insn-00bcbd44) → `01126308`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth7g_authsE` · 推定型 `undefined8`
- [`00bcbd44`](#insn-00bcbd44) → `01126310`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcbd48`](#insn-00bcbd48) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd50`](#insn-00bcbd50) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd5c`](#insn-00bcbd5c) → [`00c5a880`](../00c5a/00c5a880.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a880` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd64`](#insn-00bcbd64) → `00c9b5a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcbd68`](#insn-00bcbd68) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbd6c`](#insn-00bcbd6c) → `01126320`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase4auth13g_auths_mutexE` · 推定型 `undefined8`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbce4`](#insn-00bcbce4)

~~~json
{
  "source": "00bcbce4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbce8`](#insn-00bcbce8)

~~~json
{
  "source": "00bcbce8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd00`](#insn-00bcbd00)

~~~json
{
  "source": "00bcbd00",
  "target": "011262e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbd10`](#insn-00bcbd10)

~~~json
{
  "source": "00bcbd10",
  "target": "011262e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbd10`](#insn-00bcbd10)

~~~json
{
  "source": "00bcbd10",
  "target": "002bc0ca",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd10`](#insn-00bcbd10)

~~~json
{
  "source": "00bcbd10",
  "target": "011262f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbd10`](#insn-00bcbd10)

~~~json
{
  "source": "00bcbd10",
  "target": "00bca0a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbd14`](#insn-00bcbd14)

~~~json
{
  "source": "00bcbd14",
  "target": "011262f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011262f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbd14`](#insn-00bcbd14)

~~~json
{
  "source": "00bcbd14",
  "target": "00bca0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbd18`](#insn-00bcbd18)

~~~json
{
  "source": "00bcbd18",
  "target": "01126300",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126300",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbd1c`](#insn-00bcbd1c)

~~~json
{
  "source": "00bcbd1c",
  "target": "00c5a7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbd24`](#insn-00bcbd24)

~~~json
{
  "source": "00bcbd24",
  "target": "00c9b5a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcbd24`](#insn-00bcbd24)

~~~json
{
  "source": "00bcbd24",
  "target": "01126308",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126308",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbd30`](#insn-00bcbd30)

~~~json
{
  "source": "00bcbd30",
  "target": "00bca0b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbd38`](#insn-00bcbd38)

~~~json
{
  "source": "00bcbd38",
  "target": "01126310",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126310",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbd3c`](#insn-00bcbd3c)

~~~json
{
  "source": "00bcbd3c",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcbd40`](#insn-00bcbd40)

~~~json
{
  "source": "00bcbd40",
  "target": "01126318",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126318",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbd44`](#insn-00bcbd44)

~~~json
{
  "source": "00bcbd44",
  "target": "01126308",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126308",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbd44`](#insn-00bcbd44)

~~~json
{
  "source": "00bcbd44",
  "target": "01126310",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126310",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcbd48`](#insn-00bcbd48)

~~~json
{
  "source": "00bcbd48",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbd50`](#insn-00bcbd50)

~~~json
{
  "source": "00bcbd50",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbd5c`](#insn-00bcbd5c)

~~~json
{
  "source": "00bcbd5c",
  "target": "00c5a880",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbd64`](#insn-00bcbd64)

~~~json
{
  "source": "00bcbd64",
  "target": "00c9b5a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b5a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcbd68`](#insn-00bcbd68)

~~~json
{
  "source": "00bcbd68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbd6c`](#insn-00bcbd6c)

~~~json
{
  "source": "00bcbd6c",
  "target": "01126320",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126320",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
