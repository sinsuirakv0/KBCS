# 00a7dbec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a7d9f4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7d9f4.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0061.md#compare-a1f5f0b3de033090e5a146246f546636)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a7dc5c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a7d/00a7dc5c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0062.md#compare-9c7821e8ac3271d6662c16055016f022)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a7dbec",
  "name": "FUN_00a7dbec",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8afc0f7467494965834a3a5a4a83892ed2e6b4c3c0283a2a2d01e60ed1c09c7d",
  "source_text_sha256": "8afc0f7467494965834a3a5a4a83892ed2e6b4c3c0283a2a2d01e60ed1c09c7d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a7dbec",
        "00a7dc7f"
      ]
    ],
    "bytes_sha256": "8d454082fca7ad5c23aca8f91de1b7ffeee5a1c8fe81153d4ad0792a0e9a7570",
    "instruction_count": 37,
    "instruction_bytes": 148,
    "body_bytes": 148,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0091ff5c](../0091f/0091ff5c.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57eb0](../00c57/00c57eb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 667 bytes

~~~c

void FUN_00a7dbec(undefined8 *param_1)

{
  long lVar1;
  long *plVar2;
  
  plVar2 = (long *)param_1[0x8ba];
  *param_1 = &PTR_FUN_00c8bd00;
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53d00(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  plVar2 = (long *)param_1[0x8b8];
  if ((plVar2 != (long *)0x0) && (lVar1 = FUN_00c53d00(0xffffffffffffffff,plVar2 + 1), lVar1 == 0))
  {
    (**(code **)(*plVar2 + 0x10))(plVar2);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
  }
  FUN_0091ff5c(param_1);
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a7dbec"></a> `00a7dbec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a7dbf0"></a> `00a7dbf0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7dbf4"></a> `00a7dbf4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a7dbf8"></a> `00a7dbf8` | `14 e8 62 f9` | ldr x20,[x0, #0x45d0] | `FALL_THROUGH`
<a id="insn-00a7dbfc"></a> `00a7dbfc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a7dc00"></a> `00a7dc00` | `68 10 00 d0` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a7dc04"></a> `00a7dc04` | `08 01 34 91` | add x8,x8,#0xd00 | `FALL_THROUGH`
<a id="insn-00a7dc08"></a> `00a7dc08` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00a7dc0c"></a> `00a7dc0c` | `74 01 00 b4` | cbz x20,0x00a7dc38 | `CONDITIONAL_JUMP`
<a id="insn-00a7dc10"></a> `00a7dc10` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00a7dc14"></a> `00a7dc14` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a7dc18"></a> `00a7dc18` | `3a 58 07 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00a7dc1c"></a> `00a7dc1c` | `e0 00 00 b5` | cbnz x0,0x00a7dc38 | `CONDITIONAL_JUMP`
<a id="insn-00a7dc20"></a> `00a7dc20` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00a7dc24"></a> `00a7dc24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a7dc28"></a> `00a7dc28` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a7dc2c"></a> `00a7dc2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a7dc30"></a> `00a7dc30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a7dc34"></a> `00a7dc34` | `93 68 07 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00a7dc38"></a> `00a7dc38` | `74 e2 62 f9` | ldr x20,[x19, #0x45c0] | `FALL_THROUGH`
<a id="insn-00a7dc3c"></a> `00a7dc3c` | `74 01 00 b4` | cbz x20,0x00a7dc68 | `CONDITIONAL_JUMP`
<a id="insn-00a7dc40"></a> `00a7dc40` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00a7dc44"></a> `00a7dc44` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00a7dc48"></a> `00a7dc48` | `2e 58 07 94` | bl 0x00c53d00 | `UNCONDITIONAL_CALL`
<a id="insn-00a7dc4c"></a> `00a7dc4c` | `e0 00 00 b5` | cbnz x0,0x00a7dc68 | `CONDITIONAL_JUMP`
<a id="insn-00a7dc50"></a> `00a7dc50` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00a7dc54"></a> `00a7dc54` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a7dc58"></a> `00a7dc58` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a7dc5c"></a> `00a7dc5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00a7dc60"></a> `00a7dc60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a7dc64"></a> `00a7dc64` | `87 68 07 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00a7dc68"></a> `00a7dc68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a7dc6c"></a> `00a7dc6c` | `bc 88 fa 97` | bl 0x0091ff5c | `UNCONDITIONAL_CALL`
<a id="insn-00a7dc70"></a> `00a7dc70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a7dc74"></a> `00a7dc74` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a7dc78"></a> `00a7dc78` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a7dc7c"></a> `00a7dc7c` | `8d 68 07 14` | b 0x00c57eb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a7dbec`](#insn-00a7dbec) 範囲 `[['00a7dbec', '00a7dc0f']]`
  - `CONDITIONAL_JUMP` [`00a7dc0c`](#insn-00a7dc0c) → [`00a7dc38`](#insn-00a7dc38)
  - `FALL_THROUGH` [`00a7dc0c`](#insn-00a7dc0c) → [`00a7dc10`](#insn-00a7dc10)
- ブロック [`00a7dc10`](#insn-00a7dc10) 範囲 `[['00a7dc10', '00a7dc1f']]`
  - `CONDITIONAL_JUMP` [`00a7dc1c`](#insn-00a7dc1c) → [`00a7dc38`](#insn-00a7dc38)
  - `FALL_THROUGH` [`00a7dc1c`](#insn-00a7dc1c) → [`00a7dc20`](#insn-00a7dc20)
- ブロック [`00a7dc20`](#insn-00a7dc20) 範囲 `[['00a7dc20', '00a7dc37']]`
  - `FALL_THROUGH` [`00a7dc34`](#insn-00a7dc34) → [`00a7dc38`](#insn-00a7dc38)
- ブロック [`00a7dc38`](#insn-00a7dc38) 範囲 `[['00a7dc38', '00a7dc3f']]`
  - `CONDITIONAL_JUMP` [`00a7dc3c`](#insn-00a7dc3c) → [`00a7dc68`](#insn-00a7dc68)
  - `FALL_THROUGH` [`00a7dc3c`](#insn-00a7dc3c) → [`00a7dc40`](#insn-00a7dc40)
- ブロック [`00a7dc40`](#insn-00a7dc40) 範囲 `[['00a7dc40', '00a7dc4f']]`
  - `CONDITIONAL_JUMP` [`00a7dc4c`](#insn-00a7dc4c) → [`00a7dc68`](#insn-00a7dc68)
  - `FALL_THROUGH` [`00a7dc4c`](#insn-00a7dc4c) → [`00a7dc50`](#insn-00a7dc50)
- ブロック [`00a7dc50`](#insn-00a7dc50) 範囲 `[['00a7dc50', '00a7dc67']]`
  - `FALL_THROUGH` [`00a7dc64`](#insn-00a7dc64) → [`00a7dc68`](#insn-00a7dc68)
- ブロック [`00a7dc68`](#insn-00a7dc68) 範囲 `[['00a7dc68', '00a7dc7f']]`

## 命令位置別の参照

- [`00a7dbec`](#insn-00a7dbec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dbf0`](#insn-00a7dbf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc08`](#insn-00a7dc08) → `00c8bd00`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a7dc0c`](#insn-00a7dc0c) → [`00a7dc38`](#insn-00a7dc38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc18`](#insn-00a7dc18) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc1c`](#insn-00a7dc1c) → [`00a7dc38`](#insn-00a7dc38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc34`](#insn-00a7dc34) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc3c`](#insn-00a7dc3c) → [`00a7dc68`](#insn-00a7dc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc48`](#insn-00a7dc48) → [`00c53d00`](../00c53/00c53d00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d00` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc4c`](#insn-00a7dc4c) → [`00a7dc68`](#insn-00a7dc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc64`](#insn-00a7dc64) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc6c`](#insn-00a7dc6c) → [`0091ff5c`](../0091f/0091ff5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0091ff5c` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc74`](#insn-00a7dc74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc78`](#insn-00a7dc78) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a7dc7c`](#insn-00a7dc7c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a7dbec`](#insn-00a7dbec)

~~~json
{
  "source": "00a7dbec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dbf0`](#insn-00a7dbf0)

~~~json
{
  "source": "00a7dbf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dc08`](#insn-00a7dc08)

~~~json
{
  "source": "00a7dc08",
  "target": "00c8bd00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8bd00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a7dc0c`](#insn-00a7dc0c)

~~~json
{
  "source": "00a7dc0c",
  "target": "00a7dc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dc18`](#insn-00a7dc18)

~~~json
{
  "source": "00a7dc18",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7dc1c`](#insn-00a7dc1c)

~~~json
{
  "source": "00a7dc1c",
  "target": "00a7dc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dc34`](#insn-00a7dc34)

~~~json
{
  "source": "00a7dc34",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7dc3c`](#insn-00a7dc3c)

~~~json
{
  "source": "00a7dc3c",
  "target": "00a7dc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dc48`](#insn-00a7dc48)

~~~json
{
  "source": "00a7dc48",
  "target": "00c53d00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7dc4c`](#insn-00a7dc4c)

~~~json
{
  "source": "00a7dc4c",
  "target": "00a7dc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dc64`](#insn-00a7dc64)

~~~json
{
  "source": "00a7dc64",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7dc6c`](#insn-00a7dc6c)

~~~json
{
  "source": "00a7dc6c",
  "target": "0091ff5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a7dc74`](#insn-00a7dc74)

~~~json
{
  "source": "00a7dc74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dc78`](#insn-00a7dc78)

~~~json
{
  "source": "00a7dc78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a7dc7c`](#insn-00a7dc7c)

~~~json
{
  "source": "00a7dc7c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
