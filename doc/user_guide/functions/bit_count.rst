.. _bit_count:

BIT_COUNT
=========

``BIT_COUNT`` counts the bits set to ``1`` in the low 64 bits of an integer
value.

Syntax
------

.. code-block:: sql

   BIT_COUNT(n)

Parameters and return value
---------------------------

================== ================= ===============
Parameter / Return Type              Range
================== ================= ===============
``n``              ``DECIMAL(36,0)`` Integer input
Return             ``DECIMAL(2,0)``  ``0`` to ``64``
================== ================= ===============

The function returns the number of set bits in ``n``. It uses the low 64 bits;
bits above that range are ignored. Negative values are interpreted using a
64-bit two's-complement representation. ``NULL`` input returns ``NULL``.

Examples
--------

.. code-block:: sql

   SELECT BIT_COUNT(NULL);

Returns ``NULL``.

.. code-block:: sql

   SELECT BIT_COUNT(0);

Returns ``0`` because no bits are set.

.. code-block:: sql

   SELECT BIT_COUNT(29);

Returns ``4`` because ``29`` is ``11101`` in binary.

.. code-block:: sql

   SELECT BIT_COUNT(CAST(29 AS DECIMAL(18,0)));

Returns ``4``.

.. code-block:: sql

   SELECT BIT_COUNT(CAST(3.1415 AS DECIMAL(18,4)));

Returns ``3``. The input is converted to the function's integer parameter.

.. code-block:: sql

   SELECT BIT_COUNT(CAST(29.5 AS DOUBLE PRECISION));

Returns ``4``.

.. code-block:: sql

   SELECT BIT_COUNT(CAST(1099512676383 AS DECIMAL(36,0)));

Returns ``9``.
